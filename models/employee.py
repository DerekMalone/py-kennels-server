class Employee:
    """Member of Kennels. Stores valuable information for an
    Employee.
    """

    def __init__(self, id, name, address, location_id=None):
        self.id = id
        self.full_name = name
        self.address = address
        self.location_id = location_id
