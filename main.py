import sys

import connection


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
        with connection.get_connection() as conn:
            print("Successfully connected to the database.")
            menu()
    except connection.psycopg.OperationalError as error:
        print(f"Could not connect to the database: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
