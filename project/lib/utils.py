import sys
import re


# Function to receive a text with colon and comma and return a list with the text split.
def split_text(text_to_split):
    text_to_split = re.split('[:,]', text_to_split)
    return text_to_split


# Function to show error message to user and quit the program
def show_error_message(error_message):
    print(error_message)
    sys.exit()  # Close Program


# Function to verify if param day is weekday or weekend
def verify_weekday(date_to_verify):
    # Using regular expression to get the day of the week inside the parentheses from the inputted data
    day = date_to_verify[date_to_verify.find("(") + 1:date_to_verify.find(")")]
    if day in ['mon', 'tues', 'wed', 'thur', 'fri']:
        return 'week'
    elif day in ['sat', 'sun']:
        return 'weekend'
    else:
        return 'error'





