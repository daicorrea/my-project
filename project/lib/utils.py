import sys


# Function to format user input leaving client_type in the beginning of the list and the dates at the end.
def format_user_input(user_input):
    # Divide to know the client_type
    user_input = user_input.split(':')
    client_type = user_input.pop(0)
    # Divide to know the dates
    user_input = user_input[0].split(',')
    # Join information in only one list to return
    user_input.insert(0, client_type)
    return user_input


# Function to verify if param day inputted by the user is week day or weekend
def verify_day(user_date):
    day = user_date[user_date.find("(") + 1:user_date.find(
        ")")]  # Using regular expression to get the day of the week inside the parentheses
    if day.lower() in ['mon', 'tues', 'wed', 'thur', 'fri']:
        return 'week'
    elif day.lower() in ['sat', 'sun']:
        return 'weekend'
    else:
        return 'error'


# Function to see if the value inputted by the user has a valid format
def validate_user_input(user_input):
    if (':' and ',') in user_input:
        return True
    else:
        return False


# Function to verify if the client type is Regular or Rewards
def validate_client_type(client_type):
    if ((client_type == 'regular') or (client_type == 'rewards')):
        return True
    else:
        return False


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
