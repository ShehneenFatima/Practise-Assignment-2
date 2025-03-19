#Check if a Number is an Armstrong Number
def isArmstrong(num):
    # Convert number to string to iterate over digits
    digits = [int(digit) for digit in str(num)]
    
    # Calculate the sum of cubes of each digit
    sum_of_cubes = sum(digit ** 3 for digit in digits)
    
    # Compare with original number
    return sum_of_cubes == num

# Taking user input
num = int(input("Enter a number: "))

# Check and print result
if isArmstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

