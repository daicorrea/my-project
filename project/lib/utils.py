def format_user_input(user_input):
    user_input = user_input.split(':')
    user_type = user_input.pop(0)
    user_input = user_input[0].split(',')
    user_input.insert(0, user_type)
    print(user_input)

#Function to verify if param day is week day or weekend
def verify_day(user_date):
    day = user_date[user_date.find("(") + 1:user_date.find(")")] #Get what's in the parentheses
    if day.lower() in ['mon', 'tues', 'wed', 'thur', 'fri']:
        return 'week'
    elif day.lower() in ['sat', 'sun']:
        return 'weekend'
    else:
        return 'error'

def verify_user_input(user_input):
    if (':' and ',') in user_input:
        return True
    else:
        return False