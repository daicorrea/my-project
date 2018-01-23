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