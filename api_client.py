import requests

ORDERS_URL = "https://api.sondahub.com/v1/store/orders"

def get_orders():

    response = requests.get(ORDERS_URL)
    response.raise_for_status()
    orders = response.json()
    return orders


