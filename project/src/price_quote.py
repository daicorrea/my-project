from lib import utils


class PriceQuote():
    """This Class provides a way to store price quote information."""

    # Creating Constructor
    def __init__(self, property, client_type, input_list):
        self._property = property
        self._client_type = client_type
        self._desired_days = input_list
        self._price = 0
        self.quote()

    # Getters Functions
    def get_property(self):
        return self._property

    def get_client_type(self):
        return self._client_type

    def get_desired_days(self):
        return self._desired_days

    def get_final_price(self):
        return self._price

    # Function to quote price from property in the dates the user desired
    def quote(self):
        for date in self._desired_days:
            # Verify clienty type and get price according to day type
            if (self._client_type == 'regular'):
                if utils.verify_weekday(date) == 'week':
                    self._price += int(self._property.get_week_price())
                elif utils.verify_weekday(date) == 'weekend':
                    self._price += int(self._property.get_weekend_price())
                else:
                    utils.show_error_message(
                        'Sorry, I couldn\'t process your request. Please, verify if your dates are in the correct format.')
            elif (self._client_type == 'rewards'):
                if utils.verify_weekday(date) == 'week':
                    self._price += int(self._property.get_loyalty_week_price())
                elif utils.verify_weekday(date) == 'weekend':
                    self._price += int(self._property.get_loyalty_weekend_price())
                else:
                    utils.show_error_message(
                        'Sorry, I couldn\'t process your request. Please, verify if your dates are in the correct format.')
