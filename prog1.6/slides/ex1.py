
sentence = input("Please enter a sentence and for every 'E' you get a 'Hurray': ")

for character in sentence:
    if character == 'E':
        print('Hurray')
    else:
        print(character)
