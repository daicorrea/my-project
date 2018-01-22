from lib import utils
from lib import price_quote
from lib import load_data


def main():
    # Load Data Information from File
    property_list = load_data.load_database()

    # Get User Information
    user_input = input('Please enter your type of client and the desired dates: ')
    if utils.validate_user_input(user_input):  # Validate input
        input_list = utils.format_user_input(user_input)
    else:
        utils.show_error_message(
            'Sorry, I couldn\'t process your request. Please verify if you are searching in the following format: \n'
            '<client_type>: <date1>, <date2>, <date3>, ...')

    # Quote Property Prices
    quote_list = []
    client_type = input_list.pop(0).lower()  # Passing it all to lower case
    if utils.validate_client_type(client_type):
        for property in property_list:
            # --------------- COMENTAR AQUI DIREITO -------------
            quote_list.append(price_quote.PriceQuote(property, client_type, input_list))
        # Get best property according to price and star rating
        best_property_quoted = utils.get_best_property(quote_list)
        # print best property found to user
        print(best_property_quoted.get_property_name())
    else:
        utils.show_error_message(
            'Sorry, I couldn\'t process your request. Please verify if you typed your client type correctly '
            '(Regular or Rewards).')


# Only executes this project by itself. Do not allow to be imported by another program.
if __name__ == "__main__":
    main()