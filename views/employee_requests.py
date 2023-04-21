from models import Employee
import sqlite3
import json

EMPLOYEES = [
    {"id": 1, "name": "Doug", "location_id": 1},
    {"id": 2, "name": "Steve", "location_id": 2},
    {"id": 3, "name": "Hannah", "location_id": 1},
]


def get_all_employees():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_curser = conn.cursor()

        db_curser.execute(
            """
            SELECT
                e.id,
                e.name,
                e.address,
                e.location_id
            FROM employee e
            """
        )

        employees = []

        dataset = db_curser.fetchall()

        for row in dataset:
            employee = Employee(
                row["id"],
                row["name"],
                row["address"],
                row["location_id"],
            )

            employees.append(employee.__dict__)

        return employees


def get_single_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_curser = conn.cursor()

        db_curser.execute(
            """
            SELECT
                e.id,
                e.name,
                e.address,
                e.location_id
            FROM employee e
            WHERE e.id = ?
            """,
            (id,),
        )

        data = db_curser.fetchone()

        employee = Employee(
            data["id"],
            data["name"],
            data["address"],
            data["location_id"],
        )

    return employee.__dict__


def get_employee_by_location(location):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        SELECT 
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.location_id = ?
        """,
            (location,),
        )
        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(
                row["id"], row["name"], row["address"], row["location_id"]
            )
            employees.append(employee.__dict__)
    return employees


def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee


def delete_employee(id):
    """Deletes employee from list

    Args:
        id (int): employee id to be deleted
    """
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES.pop(index)
            break


def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
