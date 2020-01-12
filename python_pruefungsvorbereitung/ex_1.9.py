# a) Schreiben Sie eine Funktion, die einen Text entgegen nimmt und zurück gibt, wie viele Wörter in dem Text vorkommen.
"""
def word_count(phrase):
	return len(phrase.split(' '))

result = word_count("Hallo Welt")
print("There are", result, "words in the phrase")
"""
# b) Schreiben Sie eine Funktion, die einen Text entgegen nimmt und die Anzahl der Sätze zurück gibt.
"""
def phrase_count(text):
	return len(text.split('.')) - 1

result = phrase_count("Well well, it seems that I have the high ground. Now do not make the mistake to jump otherwise it will be a cutting experience.")
print("There are", result, "phrases in the text")
"""

# c) Schreiben Sie eine Funktion, die einen Text entgegen nimmt und der am meisten benutzter Buchstabe (mit Anzahl) zurückgibt.
def character_high_score(text):
	high_score_table = {}
	unique_letters = set(text)
	max_occurence = 0
	max_character = ''
	for character in unique_letters:
		occurence = text.count(character)
		if  occurence > max_occurence:
			max_occurence = occurence
			max_character = character

	return (max_character, max_occurence)

max_character, max_occurence = character_high_score("Hallo Weelt")
print("The character", max_character, "has occured the most with", max_occurence, "times.")