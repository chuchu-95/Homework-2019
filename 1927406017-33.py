letter = input("please input a letter: ")
if letter.islower():
    print(letter.upper())
elif letter.isupper():
    print(letter.lower())
else:
    print(letter)
