sentence = "Hallo Welt! Dies ist mein erstes Python-Programm."

# Only the first sentence
print(sentence[:11])

# Only the second sentence
print(sentence[11:])

# Only the first sentence backwards
print(sentence[11::-1])

# Only the second sentence backwards
print(sentence[-1:10:-1])

# Only every fourth letter of the second sentence
print(sentence[11::4])
