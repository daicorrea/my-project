class Property():
    """This Class provides a way to store properties - hotels, apartments, hostels, ... - informations."""

    # Creating Property constructor
    def __init__(self, property_name, property_type, local, star_rating, week_price, weekend_price,
                 loyalty_week_price, loyalty_weekend_price):
        self._property_name = property_name
        self._property_type = property_type
        self._local = local
        self._star_rating = star_rating
        self._week_price = week_price
        self._weekend_price = weekend_price
        self._loyalty_week_price = loyalty_week_price
        self._loyalty_weekend_price = loyalty_weekend_price

    # Functions to return information
    @property
    def property_name(self):
        return self._property_name

    @property
    def property_type(self):
        return self._property_type

    @property
    def property_local(self):
        return self._local

    @property
    def property_star_rating(self):
        return self._star_rating

    @property
    def week_price(self):
        return self._week_price

    @property
    def weekend_price(self):
        return self._weekend_price

    @property
    def loyalty_week_price(self):
        return self._loyalty_week_price

    @property
    def loyalty_weekend_price(self):
        return self._loyalty_weekend_price
