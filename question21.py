 #Implement a function ion2e() that takes a string as input and returns a copy of the string with
#the following change: if the entered word (input string) ends in 'ion', then 'ion' is replaced
#with 'e', otherwise it returns the same word.
def ion2e(word):
    if word.endswith("ion"):
        return word[:-3] + "e"
    return word

word = input("Enter a word: ")
print("Output:", ion2e(word))
