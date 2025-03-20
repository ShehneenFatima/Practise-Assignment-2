#. Write a program that take 10-time, name (string) and marks (integer) as an input from the
#user. Populate a list such that all even indices have name and odd indices with the
#corresponding marks. e.g. [‘Ahmad’, 29, ‘Asad’, 15, ‘Zainab’, 20]. At the end print the list.
#Hint: You can use append function of list data type
# Initialize an empty list
students_list = []


for _ in range(5):  
    name = input("Enter name: ")  
    marks = int(input("Enter marks: "))  
    
    students_list.append(name)  
    students_list.append(marks)  
print("\nFinal List:", students_list)
