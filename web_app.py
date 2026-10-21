import os
import secrets
from datetime import timedelta
from pathlib import Path
from flask import Flask, render_template, request, session
import connection
import orders_repository
import requests
import api_client

app = Flask(__name__)
secret_key_path = Path(__file__).with_name(".flask_secret_key")
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
if not app.secret_key:
    if secret_key_path.exists():
        app.secret_key = secret_key_path.read_text(encoding="utf-8").strip()
    else:
        app.secret_key = secrets.token_hex(32)
        secret_key_path.write_text(app.secret_key, encoding="utf-8")
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=30)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/daily-report")
def daily_report():
    with connection.get_connection() as conn:
        orders = orders_repository.get_todays_orders(conn)

    return render_template("daily_report.html", orders=orders)

@app.route("/request-simulation")
def request_simulate():
    return render_template("request_simulation.html")

@app.route("/register-customer", methods=["GET", "POST"])
def register_customer():
    if request.method == "GET":
        return render_template("register_customer.html")

    customer = {
        "name": request.form.get("name", "").strip(),
        "email": request.form.get("email", "").strip(),
    }
    for field in ("phone", "company", "tier", "notes"):
        value = request.form.get(field, "").strip()
        if value:
            customer[field] = value

    address_fields = ("line1", "line2", "city", "region", "postal_code", "country")
    address = {
        field: request.form.get(field, "").strip()
        for field in address_fields
        if request.form.get(field, "").strip()
    }
    if address:
        customer["address"] = address
    customer["marketing_opt_in"] = request.form.get("marketing_opt_in") == "on"

    try:
        result, token = api_client.create_customer(customer, session.get("sondahub_token"))
        if token:
            session["sondahub_token"] = token
            session.permanent = True
        created_customer = result.get("data", result) if isinstance(result, dict) else result
        return render_template(
            "register_customer.html",
            customer=created_customer,
            message="Kupac je uspešno registrovan na SondaHub API-ju.",
        )
    except requests.RequestException as error:
        details = error.response.text if error.response is not None else str(error)
        return render_template(
            "register_customer.html",
            error=f"Registracija nije uspela: {details}",
        ), 502

@app.route("/customers")
def customers():
    try:
        result = api_client.get_customers(session.get("sondahub_token"))
        customer_list = result.get("data", []) if isinstance(result, dict) else result
        return render_template("customers.html", customers=customer_list)
    except requests.RequestException as error:
        details = error.response.text if error.response is not None else str(error)
        return render_template("customers.html", customers=[], error=details), 502
