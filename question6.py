#Write a function binary2Decimal that take binary number as input and return decimal
#equivalent of the given number
def binary2Decimal(binary_str):
    return int(binary_str, 2)  # Convert binary string to decimal

# Taking user input
binary_str = input("Enter a binary number: ")

# Printing the decimal equivalent
print(f"Decimal equivalent of {binary_str} is {binary2Decimal(binary_str)}")
