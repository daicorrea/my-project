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

# Function to verify if param day is week day or weekend
def verify_day(user_date):
    day = user_date[user_date.find("(") + 1:user_date.find(")")]  # Gets what's inside the parentheses
    if day.lower() in ['mon', 'tues', 'wed', 'thur', 'fri']:
        return 'week'
    elif day.lower() in ['sat', 'sun']:
        return 'weekend'
    else:
        return 'error'

# Function to see if the value inputed by the user has a valid format
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

# ARRUMAR A BADERNA AQUI
def get_cheapest_property(quote_list):
    # Use first values as base to compare
    base_property = quote_list.pop(0)
    cheapest = base_property.get_property()
    min_price = base_property.get_final_price()

    print(base_property.get_property().get_property_name(), base_property.get_final_price())
    for property_quoted in quote_list:
        print(property_quoted.get_property().get_property_name(), property_quoted.get_final_price())
        # Gets minimum price
        if property_quoted.get_final_price() < min_price:
            min_price = property_quoted.get_final_price()
            cheapest = property_quoted.get_property()
        # If price is the same, compare by star ratings
        if property_quoted.get_final_price() == min_price:
            if (property_quoted.get_property().get_property_star_rating()) > (cheapest.get_property_star_rating()):
                min_price = property_quoted.get_final_price()
                cheapest = property_quoted.get_property()

    # RETORNAR ISSAQUE E IMPRIMIR NA MAIN
    print('min ', min_price)
    print('cheapest ', cheapest.get_property_name())

