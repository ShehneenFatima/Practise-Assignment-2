#Check if One Number is a Multiple of Another
def Multiple(a, b):
    return b % a == 0  # If remainder is 0, b is a multiple of a

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Checking and printing result
if Multiple(num1, num2):
    print(f"{num2} is a multiple of {num1}")
else:
    print(f"{num2} is not a multiple of {num1}")

