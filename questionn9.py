#mplement the following integer functions:
#i. A Function Celsius that returns the Celsius equivalent of a Fahrenheit temperature.
#ii. A Function Fahrenheit returns the Fahrenheit equivalent of a Celsius temperature.
#iii. Use these functions to write a program that prints charts showing the Fahrenheit
#equivalents of all Celsius temperatures from 0 to 100 degrees, and the Celsius equivalents
#of all Fahrenheit temperatures from 32 to 212 degrees. Print the outputs in a tabular format
#that minimizes the number of lines of output while remaining readable.
def Celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5 / 9

def Fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9 / 5) + 32

# Print the temperature conversion chart
print(f"{'Celsius':<10}{'Fahrenheit':<12} |  {'Fahrenheit':<12}{'Celsius'}")
print("-" * 50)

for c in range(0, 101, 10):  # Celsius from 0 to 100 in steps of 10
    f = Fahrenheit(c)
    f_to_c = Celsius(f)
    print(f"{c:<10}{f:<12.1f} |  {f:<12.1f}{f_to_c:.1f}")

print("-" * 50)
