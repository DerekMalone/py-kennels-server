ANIMALS = [
    {"id": 1, "name": "Snickers", "species": "Dog", "locationId": 1, "customerId": 4},
    {"id": 2, "name": "Roman", "species": "Dog", "locationId": 1, "customerId": 2},
    {"id": 3, "name": "Blue", "species": "Cat", "locationId": 2, "customerId": 1},
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

    return requested_animal


def create_animal(animal):
    """Posts new animal

    Args:
        animal (obj): name, species, customerId

    Returns:
        animal: id, name, species, customerId
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
