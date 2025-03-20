#Declare a list of 10 random integers and then find mean, median and mode of integers.
import random
import statistics  # Importing statistics module for mean, median, mode

# Generate a list of 10 random integers (between 1 and 50)
numbers = [random.randint(1, 50) for _ in range(10)]
print("List of numbers:", numbers)

# Calculate Mean, Median, and Mode
mean_value = statistics.mean(numbers)
median_value = statistics.median(numbers)
mode_value = statistics.mode(numbers)  # Returns first mode if multiple exist

# Print results
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
