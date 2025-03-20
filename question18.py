#Write a for loop that iterates over a list of strings myList and prints the first three characters
#of every word. e.g. If myList is the list ['January', 'February', 'March'] thenthe following
#should be printed:
#Jan
#Feb
#Mar
myList = ['January', 'February', 'March']

for word in myList:
    print(word[:3])

