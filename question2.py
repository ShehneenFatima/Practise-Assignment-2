def isAnagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if sorted versions of both strings are the same
    return sorted(str1) == sorted(str2)

# Example usage
print(isAnagram("listen", "silent"))  # Output: True
print(isAnagram("hello", "world"))  # Output: False
print(isAnagram("Astronomer", "Moon starer"))  # Output: True
print(isAnagram("Python", "typhon"))  # Output: True
print(isAnagram("School Master", "The Classroom"))  # Output: True
