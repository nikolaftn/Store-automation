import sys
import connection
import api_client
import requests
import orders_repository
import web_app
import webbrowser


def menu():
    print("====== STORE SERVICE ======")
    print()
    print("1 - View daily report")
    print("2 - Simulate an order")
    print("q - Quit")

    while True:
        option = input("Choose an option: ").strip().lower()

        if option == "1":
            print("Opening daily report...")
            break
        elif option == "2":
            print("Simulating an order...")
            break
        elif option == "q":
            sys.exit(0)
        else:
            print("Invalid option. Please try again.")


def main():

    try:
        orders = api_client.get_orders()
        print("API response received.")
        print("Number of orders:", len(orders["data"]))
    
    except requests.RequestException as error:
        print(f"Could not fetch orders: {error}")
        sys.exit(1)

    try:
        with connection.get_connection() as conn:
            print("Successfully connected to the database.")

            try:
                orders_repository.save_orders(conn, orders)

            except connection.psycopg.Error as error:
                print(f"Could not save data to database: {error}")

    except connection.psycopg.OperationalError as error:
        print(f"Could not connect to the database: {error}")
        sys.exit(1)


    webbrowser.open("http://127.0.0.1:5000")
    web_app.app.run(debug=False, use_reloader=False)

            


if __name__ == "__main__":
    main()


