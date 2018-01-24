# Function to see if the value inputted by the user has a valid format
def validate_user_input(user_input):
    if (':' and ',') in user_input:
        return True
    else:
        return False


# Function to verify if the client type is Regular or Rewards
def validate_client_type(client_type):
    if ((client_type == 'regular') or (client_type == 'rewards')):
        return True
    else:
        return False


# Function to verify if list has values
def validate_full_list(list_to_validate):
    if len(list_to_validate) > 0:
        return True
    else:
        return False
