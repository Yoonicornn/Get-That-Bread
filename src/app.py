def input_to_index(year, month):
    # Start year is 2017
    start_year = 2017

    # Calculate the number of months since January 2017
    months_since_start = (year - start_year) * 12 + (month - 1)

    # The index starts at 1, so add 1 to the result
    return months_since_start + 1

print(input_to_index(2030, 1))