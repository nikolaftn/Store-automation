import psycopg


def get_connection():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="store",
        user="postgres",
        password="postgres",
    )
