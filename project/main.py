from lib import read_file
from lib import hotel
from lib import utils
from lib import price_quote

def main():
    #Read database file with .csv extension to get current prices information
    file = read_file.ReadFile('../docs/database.csv')
    database = file.get_data()
    #print(database)

    #Create objects
    property_list = [] #List of hotels
    for data in database:
        property_list.append(hotel.Hotel(data[0], data[1], data[2], data[3], data[4],
                                      data[5], data[6], data[7]))

    #print(property_list[0].get_info())

    #Get User Information
    user_input = input('Please enter your type of client and the desired dates: ')
    if utils.verify_user_input(user_input):
        utils.format_user_input(user_input)
    else:
        print('Sorry, we couldn\'t process your request. Please verify how you wrote your search and try again.')

    #Quote property prices
    #for property in property_list:
        #price_quote.PriceQuote(property)


    #Find Week Day
    #day = user_input[user_input.find("(") + 1:user_input.find(")")]
    #print(day)



    #print(property_list.get_info())

#Only executes this project by itself. Do not allow to be imported by another program.
if __name__ == "__main__":
    main()
