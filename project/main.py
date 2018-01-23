from lib import utils
from helpers import validate
from helpers import search_property
from src import price_quote
from src import load_data


def main():
    # Load Data Information from File
    property_list = load_data.load_database()

    # Get User Information
    user_input = input(
        'Please enter your type of client and the desired dates: ').lower()  # Already getting the input in lower case
    if validate.validate_user_input(user_input):  # Validate input
        # Split input text in a list leaving the client type in the beginning
        input_list = utils.split_text(user_input)
    else:
        utils.show_error_message(
            'Sorry, I couldn\'t process your request. Please verify if you are searching in the following format: \n'
            '<client_type>: <date1>, <date2>, <date3>, ...')

    # Quote Property Prices
    quote_list = []
    client_type = input_list.pop(0)
    if validate.validate_client_type(client_type):
        for property in property_list:
            # --------------- COMENTAR AQUI DIREITO -------------
            quote_list.append(price_quote.PriceQuote(property, client_type, input_list))
        # Get best property according to price and star rating
        best_property_quoted = search_property.property_by_price(quote_list)
        # print best property found to user
        print(best_property_quoted.property_name)
    else:
        utils.show_error_message(
            'Sorry, I couldn\'t process your request. Please verify if you typed your client type correctly '
            '(Regular or Rewards).')


# Only executes this project by itself. Do not allow to be imported by another program.
if __name__ == "__main__":
    main()
