# a
def encript_sentence(sentence):
    # We use lower because we want to ignore if the character is upper or lower case
    modified_sentence = ''
    for character in sentence:
        if character.lower() == 'e':
            modified_sentence += '3'
        elif character.lower() == 'a':
            modified_sentence += '4'
        elif character.lower() == 'o':
            modified_sentence += '0'
        elif character.lower() == 'i':
            modified_sentence += '1'
        elif character.lower() == 's':
            modified_sentence += '5'
        else:
            modified_sentence += character
    return modified_sentence

sentence = input("Please enter a sentence whe should encript: ")
result = encript_sentence(sentence)
print("Your encrypted sentence is:", result)
