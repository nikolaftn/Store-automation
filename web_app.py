from flask import Flask, render_template
import connection
import orders_repository

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/daily-report")
def daily_report():
    with connection.get_connection() as conn:
        orders = orders_repository.get_todays_orders(conn)

    return render_template("daily_report.html", orders=orders)
