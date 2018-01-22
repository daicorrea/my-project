from lib import read_file
from lib import hotel
from lib import utils


# Function to read file into a list and return that list.
def load_database():
    filename = '../docs/database.csv'
    if validate_file(filename):
        # Read database file with .csv extension to get current prices information
        file = read_file.ReadFile(filename)
        database = file.get_data()

        # Create Hotel objects
        property_list = []  # Create list to return data

        # --------------------------------------------------
        # ---------- VERIFICAR SE A ENTRADA TEM 8 ----------
        # --------------------------------------------------

        for data in database:
            property_list.append(hotel.Hotel(data[0], data[1], data[2], data[3], data[4],
                                             data[5], data[6], data[7]))
        return property_list
    else:
        # If file is not valid, show an error and close the program.
        utils.show_error_message('It was not possible to load data. Verify if you have a .csv file to load.')

# Function to validate if the database desired file is a csv file
def validate_file(filename):
    if (filename.endswith('.csv')):
        return True
    else:
        return False
