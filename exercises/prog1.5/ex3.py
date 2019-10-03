vocals = list("aeiou")
character = input("Please enter a character: ")

if character == 'y':
    print("Y is sometimes a vocal and sometimes a consonant")
elif character in vocals:
    print("The character", character, "is a vocal")
else:
    print("Your character is not a vocal")
