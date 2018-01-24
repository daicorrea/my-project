from helpers import load_data
from helpers import validate
from helpers import text_analyzer
from helpers import search_property
from helpers import dynamic_message
from src import price_quote


def main():
    # Load Data Information from File
    property_list = load_data.load_database('./docs/database.csv')


    # Get User Information in lower case to facilitate validations
    user_input = input(
        'Please enter your type of client and the desired dates: ').lower()

    if validate.validate_user_input(user_input):  # Validate input
        # Split input text in a list leaving the client type in the beginning
        input_list = text_analyzer.split_text(user_input)
    else:
        dynamic_message.show_error_message_and_quit(
            'Sorry, I couldn\'t process your request. Please verify if you are searching in the following format: \n'
            '<client_type>: <date1>, <date2>, <date3>, ...')

    # Quote Property Prices
    quote_list = []
    # Verify if client option inputted is okay
    client_type = input_list.pop(0)
    if validate.validate_client_type(client_type):
        for property in property_list:
            # Store in a list the quoted price for each property for the dates and client type inputted
            quote_list.append(price_quote.PriceQuote(property, client_type, input_list))
        # Get best property according to price and star rating
        best_property_quoted = search_property.property_by_price(quote_list)
        # print best property found to user
        print(best_property_quoted.property_name)
    else:
        dynamic_message.show_error_message_and_quit(
            'Sorry, I couldn\'t process your request. Please verify if you typed your client type correctly '
            '(Regular or Rewards).')


# Only executes this project by itself. Do not allow to be imported by another program.
if __name__ == "__main__":
    main()
