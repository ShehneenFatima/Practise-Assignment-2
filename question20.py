# Write a program that requests an integer n from the user and append the squares of all
#numbers from 0 up to, but not including, n. At the end print the list.
 n = int(input("Enter n: "))  
squares = [i**2 for i in range(n)]  

print(squares)

