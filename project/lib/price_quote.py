from lib import utils
import sys

class PriceQuote():
    """This Class provides a way to store price quote information."""

    # Creating Constructor
    def __init__(self, property, client_type, input_list):
        self.property = property
        self.client_type = client_type
        self.desired_days = input_list
        self.price = 0
        self.quote()

    # Function to quote price from property in the dates the user desired
    def quote(self):
        for date in self.desired_days:
            if (self.client_type == 'regular'):
                if utils.verify_day(date) == 'week':
                    self.price += int(self.property.get_week_price())
                elif utils.verify_day(date) == 'weekend':
                    self.price += int(self.property.get_weekend_price())
                else:
                    print('Sorry, I couldn\'t process your request. Please, verify if your dates are in the correct format.')
                    sys.exit()  # Close Program
            elif (self.client_type == 'rewards'):
                if utils.verify_day(date) == 'week':
                    self.price += int(self.property.get_loyalty_week_price())
                elif utils.verify_day(date) == 'weekend':
                    self.price += int(self.property.get_loyalty_weekend_price())
                else:
                    print('Sorry, I couldn\'t process your request. Please, verify if your dates are in the correct format.')
                    sys.exit()  # Close Program

    #GETTERS AQUI COMENTAR
    def get_final_price(self):
        return self.price

    def get_property(self):
        return self.property

