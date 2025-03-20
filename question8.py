#Print a Solid Square of a Given Character
def print_square(side, char):
    for _ in range(side):  # Loop to print 'side' number of rows
        print(char * side)  # Print a row of repeated characters

# Taking user input
side = int(input("Enter the size of the square: "))
char = input("Enter the character to print: ")[0]  # Take only the first character

# Printing the square
print_square(side, char)

