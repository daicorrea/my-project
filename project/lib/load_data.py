from lib import read_file
from lib import hotel
import sys

#Function to read file into a list and return that list.
def load_database():
    filename = '../docs/database.csv'
    # Read database file with .csv extension to get current prices information
    if validate_file(filename):
        file = read_file.ReadFile(filename)
        database = file.get_data()

        # Create Hotel objects
        property_list = []
        for data in database:
            property_list.append(hotel.Hotel(data[0], data[1], data[2], data[3], data[4],
                                             data[5], data[6], data[7]))
        return property_list
    else:
        print('It was not possible to load data. Verify if you have a .csv file to load.')
        sys.exit()

#Function to validate if the database desired file is a csv file
def validate_file(filename):
    if (filename.endswith('.csv')):
        return True
    else:
        return False