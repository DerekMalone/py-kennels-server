from .customer_requests import get_single_customer
from .location_requests import get_single_location

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


def get_all_animals():
    return ANIMALS


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
def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal
            requested_animal["customer"] = get_single_customer(
                requested_animal["customerId"]
            )
            requested_animal["location"] = get_single_location(
                requested_animal["locationId"]
            )
            if "customerId" in requested_animal:
                del requested_animal["customerId"]
            if "locationId" in requested_animal:
                del requested_animal["locationId"]
            break

    return requested_animal


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
    # Initial -1 value for animal index, in case one isn't found
    animal_index = None
    # animal_index = -1

    # Iterate the ANIMAL list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            animal_index = index
            break

    if animal_index:
        ANIMALS.pop(animal_index)
    # if animal_index >= 0:
    #     ANIMALS.pop(animal_index)

    # HACK: above is the same as below, above has unnecessary redundancy
    #    for index, animal in enumerate(ANIMALS):
    #        if animal["id"] == id:
    #           ANIMALS.pop(index)


def update_animal(id, new_animal):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            ANIMALS[index] = new_animal
            break  # NOTE: This break is to stop the for loop from continuing after
            # the item to be updated has been found.
