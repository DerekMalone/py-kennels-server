from .customer_requests import get_single_customer
from .location_requests import get_single_location
from models import Animal, Location
import sqlite3
import json

ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted",
    },
    {
        "id": 2,
        "name": "Roman",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted",
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted",
    },
]

# def get_all_animals():
#     return ANIMALS


def get_all_animals():
    # NOTE: Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:
        # NOTE: listed as a black box. Should still look into...
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # NOTE: Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address
        FROM animal a
        JOIN location l
        ON a.location_id = l.id
        """
        )

        # NOTE: Initialize an empty list to hold all animal representations
        animals = []

        # NOTE: Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # NOTE: Iterate list of data returned from database
        for row in dataset:
            # NOTE: Create an animal instance from the current row.
            # NOTE: Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(
                row["id"],
                row["name"],
                row["breed"],
                row["status"],
                row["location_id"],
                row["customer_id"],
            )

            location = Location(
                row["location_id"], row["location_name"], row["location_address"]
            )

            animal.location = location.__dict__

            animals.append(animal.__dict__)

        return animals


def get_animal_by_location(location):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.location_id = ?
        """,
            (location,),
        )

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(
                row["id"],
                row["name"],
                row["breed"],
                row["status"],
                row["location_id"],
                row["customer_id"],
            )
            animals.append(animal.__dict__)

    return animals


def get_animal_by_status(status):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.status = ?
        """,
            (status,),
        )

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(
                row["id"],
                row["name"],
                row["breed"],
                row["status"],
                row["location_id"],
                row["customer_id"],
            )
            animals.append(animal.__dict__)

    return animals


# # REVIEW: Need to ask Hannah to explain this.
# a = ("MNNIT Allahabad", 5000, "Engineering")

# # HACK: a = ("NSS", 2000, "Software Development") => this does not reassign the value it just
# # HACK: creates a new variable of a and erases the previous one.

# # this lines UNPACKS values
# # of variable a
# (
#     college,
#     student,
#     type_ofcollege,
# ) = a  # HACK: This is just called deconstruction where each item on the left is a variable

# # HACK: an array is called a list in Python.

# # print college name
# print(college)

# # print no of student
# print(student)

# # print type of college
# print(type_ofcollege)


# Function with a single parameter
# def get_single_animal(id):
#     # Variable to hold the found animal, if it exists
#     requested_animal = None

#     # Iterate the ANIMALS list above. Very similar to the
#     # for..of loops you used in JavaScript.
#     for animal in ANIMALS:
#         # Dictionaries in Python use [] notation to find a key
#         # instead of the dot notation that JavaScript used.
#         if animal["id"] == id:
#             requested_animal = animal.copy()
#             requested_animal["customer"] = get_single_customer(
#                 requested_animal["customerId"]
#             )
#             requested_animal["location"] = get_single_location(
#                 requested_animal["locationId"]
#             )
#             if "customerId" in requested_animal:
#                 del requested_animal["customerId"]
#             if "locationId" in requested_animal:
#                 del requested_animal["locationId"]
#             break

#     return requested_animal


def get_single_animal(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute(
            """
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address
        FROM animal a
        JOIN Location l
        On a.location_id = l.id
        WHERE a.id = ?
        """,
            (id,),
        )

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(
            data["id"],
            data["name"],
            data["breed"],
            data["status"],
            data["location_id"],
            data["customer_id"],
        )

        location = Location(
            data["location_id"], data["location_name"], data["location_address"]
        )

        animal.location = location.__dict__

        return animal.__dict__


def create_animal(new_animal):
    """Posts new animal

    Args:
        animal (dict): animal to be added to list

    Returns:
        animal with id on it
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        INSERT INTO Animal
            ( name, breed, status, location_id, customer_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """,
            (
                new_animal["name"],
                new_animal["breed"],
                new_animal["status"],
                new_animal["locationId"],
                new_animal["customerId"],
            ),
        )

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_animal["id"] = id

    return new_animal


def delete_animal(id):
    """Deletes and animal from ANIMALS List

    Args:
        id (int): animal id
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        DELETE FROM animal
        WHERE id = ?
        """,
            (id,),
        )


def update_animal(id, new_animal):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """,
            (
                new_animal["name"],
                new_animal["breed"],
                new_animal["status"],
                new_animal["locationId"],
                new_animal["customerId"],
                id,
            ),
        )

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
