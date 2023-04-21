from models import Customer
import sqlite3
import json

CUSTOMERS = [{"id": 1, "name": "Ryan Tanay"}]


def get_all_customers():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_curser = conn.cursor()

        db_curser.execute(
            """
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        """
        )

        customers = []

        dataset = db_curser.fetchall()

        for row in dataset:
            customer = Customer(
                row["id"],
                row["name"],
                row["address"],
                row["email"],
                row["password"],
            )

            customers.append(customer.__dict__)

        return customers


def get_single_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c 
        WHERE c.id = ?
        """,
            (id,),
        )

        data = db_cursor.fetchone()

        customer = Customer(
            data["id"],
            data["name"],
            data["address"],
            data["email"],
            data["password"],
        )

        return customer.__dict__


def get_customers_by_email(email):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """,
            (email,),
        )

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(
                row["id"], row["name"], row["address"], row["email"], row["password"]
            )
            customers.append(customer.__dict__)

    return customers


def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer


def delete_customer(id):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS.pop(index)
            break


def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
