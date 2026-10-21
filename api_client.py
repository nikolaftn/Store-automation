import requests

ORDERS_URL = "https://api.sondahub.com/v1/store/orders"
CUSTOMERS_URL = "https://api.sondahub.com/v1/store/customers"

def get_orders():

    response = requests.get(ORDERS_URL)
    response.raise_for_status()
    orders = response.json()
    return orders


def create_customer(customer, session_token=None):
    headers = {"X-Sondahub-Session": session_token} if session_token else {}
    response = requests.post(CUSTOMERS_URL, json=customer, headers=headers, timeout=15)
    response.raise_for_status()
    return response.json(), response.headers.get("X-Sondahub-Session")


def get_customers(session_token=None):
    headers = {"X-Sondahub-Session": session_token} if session_token else {}
    response = requests.get(
        CUSTOMERS_URL,
        params={"sort": "-id", "limit": 100},
        headers=headers,
        timeout=15,
    )
    response.raise_for_status()
    return response.json()

