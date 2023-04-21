from .customer_requests import get_single_customer
from .location_requests import get_single_location
from models import Animal
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
            a.customer_id
        FROM animal a
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
            a.customer_id
        FROM animal a
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

        return animal.__dict__


def create_animal(animal):
    """Posts new animal

    Args:
        animal (dict): animal to be added to list

    Returns:
        animal with id on it
    """
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with 'id' property added
    return animal


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
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            ANIMALS[index] = new_animal
            break  # NOTE: This break is to stop the for loop from continuing after
            # the item to be updated has been found.
