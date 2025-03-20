
#Write a function that takes a decimal number as input and returns its octal equivalent.
def decimal_to_octal(num):
    return oct(num)[2:]  # Convert to octal and remove '0o' prefix

# Taking user input
num = int(input("Enter a number: "))

# Printing the octal equivalent
print(f"Octal equivalent of {num} is {decimal_to_octal(num)}")
