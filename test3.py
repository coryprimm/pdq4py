import pdq4py
import random
import string

# Create a list of mixed data types (strings, ints, and floats)
data = [True, 100, {1:'2'}]

# Attempt to sort the mixed data types using pdqsort
try:
    sorted_data = pdq4py.pdqSort(data)
    print(sorted_data)
except Exception as e:
    print(f"An error occurred: {str(e)}")