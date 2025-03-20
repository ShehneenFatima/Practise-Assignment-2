#Write a function that takes a tuple of 10 number as a parameter and return the minimum of all
#the numbers.
def find_minimum(numbers):
    """Return the minimum value from a tuple of numbers."""
    return min(numbers)

# Define a tuple with 10 numbers
numbers_tuple = (12, 45, 7, 89, 23, 5, 67, 34, 8, 19)

# Find and print the minimum value
print("Tuple:", numbers_tuple)
print("Minimum value:", find_minimum(numbers_tuple))

