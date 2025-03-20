#Write a function named custom_range() that takes three parameters:
def custom_range(start, stop, step):
    numbers = []  # Initialize an empty list
    if step == 0:
        raise ValueError("Step cannot be zero")  # Prevent infinite loop
    
    if start < stop and step > 0:  # Increasing range
        while start < stop:
            numbers.append(start)
            start += step
    elif start > stop and step < 0:  # Decreasing range
        while start > stop:
            numbers.append(start)
            start += step
    
    return numbers

# Example usage
print(custom_range(1, 10, 2))  # Output: [1, 3, 5, 7, 9]
print(custom_range(5, 0, -1))  # Output: [5, 4, 3, 2, 1]
print(custom_range(0, 20, 5))  # Output: [0, 5, 10, 15]
