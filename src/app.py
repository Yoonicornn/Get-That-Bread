def input_to_index_bread(year, month):
    # Start year is 2017
    start_year = 2017

    # Calculate the number of months since January 2017
    months_since_start = (year - start_year) * 12 + (month - 1)

    # The index starts at 1, so add 1 to the result
    return months_since_start + 1

def input_to_index_sp(year, month):
    # Start year is 2009
    start_year = 2009

    # Calculate the number of months since February 2009
    months_since_start = (year - start_year) * 12 + (month - 1)

    return months_since_start

# print(input_to_index_sp(2023, 11))
# print(input_to_index_bread(2022, 12))