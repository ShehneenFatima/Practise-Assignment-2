def isIn(str1, str2):
    return str1 in str2 or str2 in str1  # Check if either string is a substring of the other

# Example usage
print(isIn("hello", "hello world"))  # Output: True
print(isIn("world", "hello"))  # Output: False
print(isIn("abc", "abcdef"))  # Output: True
print(isIn("test", "testing"))  # Output: True
print(isIn("Python", "I love Python!"))  # Output: True
