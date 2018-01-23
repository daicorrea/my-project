from src import property


class Hotel(property.Property):
    """This Class provides a way to store hotel informations based on a property."""

    # Creating Constructor
    def __init__(self, property_name, property_type, local, star_rating, week_price, weekend_price,
                 loyalty_week_price, loyalty_weekend_price):
        # Calling property constructor for heritage
        property.Property.__init__(self, property_name, property_type, local, star_rating, week_price, weekend_price,
                                   loyalty_week_price, loyalty_weekend_price)