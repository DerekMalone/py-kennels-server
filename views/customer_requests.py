from models import Customer
import sqlite3
import json

CUSTOMERS = [{"id": 1, "name": "Ryan Tanay"}]


# def get_all_customers():
#     return CUSTOMERS


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
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
            break

    return requested_customer


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
