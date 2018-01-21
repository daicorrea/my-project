class Property():
    """This Class provides a way to store properties - hotels, apartments, hostels, ... - informations."""

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

    def get_info(self):
        return self.property_name

    def verify_price(self, date):
        print(date)