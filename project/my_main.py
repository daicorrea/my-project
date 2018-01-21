from lib import read_file
from lib import property

def main():
    #Read database file with .csv extension to get current prices information
    file = read_file.ReadFile('../docs/database.csv')
    database = file.get_data()
    #print(database)

    #Create objects
    property_list = property.Property('prop_name')
    print(property_list.get_info())

#Only executes this project by itself. Do not allow to be imported by another program.
if __name__ == "__main__":
    main()
