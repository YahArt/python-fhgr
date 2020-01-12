# a) Schreiben Sie eine Funktion, die einen Text entgegen nimmt und einen Text zurück gibt, von dem folgende Sonderzeichen entfernt wurden
def clean_text(text):
	ignore_list = list('!?.,:; _')
	for character in ignore_list:
		text = text.replace(character, '')

	return text

result = clean_text('!?.,:; _hallowelt!?.,:; _')
print(result)

# b) Erweitern Sie die Funktion sodass Umlaute umgewandelt werden
"""
def clean_text(text):
	ignore_list = list('!?.,:; _')
	for character in text:
		if character in ignore_list:
			text = text.replace(character, '')
		
	# Clean all vocals
	text = text.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
	return text

result = clean_text('!?.,:; _hallöwelt!?.,:; _')
print(result)
"""