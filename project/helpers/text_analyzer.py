import re


# Function to receive a text with colon and comma and return a list with the text split.
def split_text(text_to_split):
    text_to_split = re.split('[:,]', text_to_split)
    return text_to_split
