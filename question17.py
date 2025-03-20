# Take a name (i.e., a string) as an input from the user and insert it into a list, then pass this list
#to a function swap that exchange the first and last values of list. After swapping print the
#resultant list.
def swap(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

names_list = input("Enter names (comma-separated): ").split(", ")

print("Before Swapping:", names_list)
print("After Swapping:", swap(names_list))
