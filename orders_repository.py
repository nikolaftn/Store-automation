import connection
from psycopg.types.json import Jsonb

def save_orders(connection, orders):
    print("save_orders() started.")
    print("Orders to save:", len(orders["data"]))
    with connection.cursor() as cursor:
        for order in orders["data"]:
            cursor.execute(
                """
            INSERT INTO orders (
                id, order_number, customer_id, status,
                subtotal, shipping, tax, discount, total, currency,
                payment_method, shipping_method, tracking_number,
                created_at, updated_at, placed_at, paid_at,
                shipped_at, delivered_at, shipping_address, notes
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
            ON CONFLICT (id) DO NOTHING

                """,
                (
                    order["id"],
                    order["number"],
                    order["customer_id"],
                    order["status"],
                    order["subtotal"],
                    order["shipping"],
                    order["tax"],
                    order["discount"],
                    order["total"],
                    order["currency"],
                    order["payment_method"],
                    order["shipping_method"],
                    order["tracking_number"],
                    order["created_at"],
                    order["updated_at"],
                    order["placed_at"],
                    order["paid_at"],
                    order["shipped_at"],
                    order["delivered_at"],
                    Jsonb(order["shipping_address"]),
                    order["notes"],
                ),
            )


def get_todays_orders(conn):
    with conn.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, customer_id, order_number, status, total, currency, placed_at
            FROM orders
            WHERE placed_at::date = CURRENT_DATE
            ORDER BY placed_at
            """
        )
        return cursor.fetchall()