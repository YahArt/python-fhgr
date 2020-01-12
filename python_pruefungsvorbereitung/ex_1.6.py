# Schreiben Sie ein Programm, dass ein Wort entgegen nimmt und zurück gibt, ob das Wort ein Palindrom ist oder nicht (ein Palindrom liest sich von vorne und von hinten gleich: ABBA)

word = input("Please enter a word: ")

palyndrom = word.lower()[::-1]

if word.lower() == palyndrom:
	print("The word", word, "is a palyndrom")
else:
	print("The word", word, "is not a palyndrom")
