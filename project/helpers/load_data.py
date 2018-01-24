from helpers import dynamic_message
from lib import read_file
from src import hotel


# Function to read file into a list and return that list.
def load_database(filename):
    if validate_file_extension(filename, '.csv'):
        # Read database file with .csv extension to get current prices information
        file = read_file.ReadFile(filename)
        database = file.get_data()
        # Creating the hotel objects
        property_list = create_properties(database)
        return property_list
    else:
        # If file is not valid, show an error and close the program.
        dynamic_message.show_error_message_and_quit('It was not possible to load data. Verify if you have a .csv file to load.')


# Function to create objects
def create_properties(database):
    property_list = []  # Create list to return data
    for data in database:
        # Verify if the document has 8 columns
        if validate_list_quantity(data, 8):
            # Removing data column name line using first identity column item in the list.
            if 'property_name' not in data[0].lower():
                # Verify if type is a hotel before creating a hotel type object
                if data[1].lower() == 'hotel':
                    # Using argument unpacking to pass the attributes to create the hotels and add to the property list
                    property_list.append(hotel.Hotel(*data))
                else:
                    print('We are only processing hotel at the moment. Please, contact the administrator.')
        else:
            dynamic_message.show_error_message_and_quit(
                'It was not possible to load data. Verify if your file input is in the correct format.')
    return property_list


# Function to validate if the database desired ffile has the right extension
def validate_file_extension(filename, extension):
    if (filename.endswith(extension)):
        return True
    else:
        return False


# Function to validate quantity of items in a list
def validate_list_quantity(list_to_validate, qtd_items):
    if len(list_to_validate) == qtd_items:
        return True
    else:
        return False
