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








