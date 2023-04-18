from models import Location
import sqlite3
import json

LOCATIONS = [
    {"id": 1, "name": "Nashville North", "address": "8422 Johnson Pike"},
    {"id": 2, "name": "Nashville South", "address": "209 Emory Drive"},
]


def get_all_locations():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_curser = conn.cursor()

        db_curser.execute(
            """
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        """
        )

        locations = []

        dataset = db_curser.fetchall()

        for row in dataset:
            location = Location(
                row["id"],
                row["name"],
                row["address"],
            )

            locations.append(location.__dict__)

        return locations


# Function with a single parameter
def get_single_location(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_curser = conn.cursor()

        db_curser.execute(
            """
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """,
            (id,),
        )

        data = db_curser.fetchone()

        location = Location(
            data["id"],
            data["name"],
            data["address"],
        )

        return location.__dict__


def create_location(location):
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return location


# def delete_location(id):
#     location_index = None
#     for index, location in enumerate(LOCATIONS):
#         if location["id"] == id:
#             location_index = index

#     if location_index:
#         LOCATIONS.pop(location_index)


def delete_location(id):
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS.pop(index)
            break


def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break
