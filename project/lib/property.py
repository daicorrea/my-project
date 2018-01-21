class Property():
    """This Class provides a way to store properties - hotels, apartments, hostels, ... - informations."""

    def __init__(self, property_name):
        self.property_name = property_name

    def get_info(self):
        return self.property_name