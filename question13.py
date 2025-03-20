 #Declare a list of 20 integers that has duplicate numbers, write a program to delete duplicate
#numbers from list.
def remove_duplicates(lst):
    """Remove duplicates from a list while keeping unique values."""
    return list(set(lst))

# Declare a list of 20 integers with duplicates
numbers = [5, 12, 7, 12, 8, 5, 19, 7, 14, 8, 20, 5, 7, 25, 14, 8, 9, 19, 25, 10]

# Print original list
print("Original list:", numbers)

# Remove duplicates
unique_numbers = remove_duplicates(numbers)

# Print updated list
print("List after removing duplicates:", unique_numbers)
