class Employee:
    """Member of Kennels. Stores valuable information for an
    Employee.
    """

    def __init__(self, id, name, location_id=None):
        self.id = id
        self.full_name = name
        self.location_id = location_id
