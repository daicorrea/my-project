class Property():
    """This Class provides a way to store properties - hotels, apartments, hostels, ... - informations."""

    #Creating Constructor
    def __init__(self, property_name, property_type, local, star_rating, week_price, weekend_price,
                 loyalty_week_price, loyalty_weekend_price):
        self.property_name = property_name
        self.property_type = property_type
        self.local = local
        self.star_rating = star_rating
        self.week_price = week_price
        self.weekend_price = weekend_price
        self.loyalty_week_price = loyalty_week_price
        self.loyalty_weekend_price = loyalty_weekend_price

    #Funtions to return information
    def get_property_name(self):
        return self.property_name

    def get_property_type(self):
        return self.property_type

    def get_property_local(self):
        return self.property_local

    def get_property_star_rating(self):
        return self.star_rating

    def get_week_price(self):
        return self.week_price

    def get_weekend_price(self):
        return self.weekend_price

    def get_loyalty_week_price(self):
        return self.loyalty_week_price

    def get_loyalty_weekend_price(self):
        return self.loyalty_weekend_price

