import sys
import re


# Function to receive a text with colon and comma and return a list with the text split.
def split_text(text_to_split):
    text_to_split = re.split('[:,]', text_to_split)
    return text_to_split


# Function to verify if param day inputted by the user is week day or weekend
def verify_day(user_date):
    # Using regular expression to get the day of the week inside the parentheses from the inputted data
    day = user_date[user_date.find("(") + 1:user_date.find(")")]
    if day in ['mon', 'tues', 'wed', 'thur', 'fri']:
        return 'week'
    elif day in ['sat', 'sun']:
        return 'weekend'
    else:
        return 'error'


# Function to quote the best property according to price and star rating
def get_best_property(quote_list):
    # Use first value of the list as base to compare with the other values
    base_property = quote_list.pop(0)  # Removed from the list to not be compared again
    best_property_quoted = base_property.get_property()
    min_price_quoted = base_property.get_final_price()

    # Compare each property in the list with the first one
    for property_quoted in quote_list:
        # Gets minimum price
        if property_quoted.get_final_price() < min_price_quoted:
            min_price_quoted = property_quoted.get_final_price()
            best_property_quoted = property_quoted.get_property()

        # If both properties have the same, compare them and choose the one with the highest star rating
        if property_quoted.get_final_price() == min_price_quoted:
            if (property_quoted.get_property().get_property_star_rating()) > (
                    best_property_quoted.get_property_star_rating()):
                min_price_quoted = property_quoted.get_final_price()
                best_property_quoted = property_quoted.get_property()

    return best_property_quoted


# Function to show error message to user and quit the program
def show_error_message(error_message):
    print(error_message)
    sys.exit()  # Close Program
