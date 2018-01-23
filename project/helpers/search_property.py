# Function to quote the best property according to price.
# In case there are more than one property with the cheapest price, the one with the highest star rating will be returned.
def property_by_price(quoted_list):
    # Use first value of the list as base to compare with the other values
    base_property = quoted_list.pop(0)  # Removed from the list to not be compared again
    best_property_quoted = base_property.get_property()
    min_price_quoted = base_property.get_final_price()

    # Compare each property in the list with the first one
    for property_quoted in quoted_list:
        # Get property with the minimum price
        if property_quoted.get_final_price() < min_price_quoted:
            min_price_quoted = property_quoted.get_final_price()
            best_property_quoted = property_quoted.get_property()

        # If both properties have the same, compare them and choose the one with the highest star rating
        if property_quoted.get_final_price() == min_price_quoted:
            if (property_quoted.get_property().property_star_rating) > (
                    best_property_quoted.property_star_rating):
                min_price_quoted = property_quoted.get_final_price()
                best_property_quoted = property_quoted.get_property()

    return best_property_quoted
