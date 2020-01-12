# a) Schreiben Sie ein eine Funktion, die eine beliebige Liste von Wörtern entgegen nimmt und die doppelten Wörter aus der Liste entfernt. Die entduplizierte Liste soll dann zurück gegeben werden.
def unique_list(list_with_duplicated_elements):
	return list(set(list_with_duplicated_elements))

result = unique_list(["Hallo", "hallo", "Welt", "welt"])
print(result)


# b) Erweitern Sie die Funktion sodass doppelte Wörter entfernt werden und dabei nicht auf die Gross- und Kleinschreibung geachtet wird.
"""
def unique_list(list_with_duplicated_elements):
	unique_list = []
	for element in list_with_duplicated_elements:
		if element.lower() not in unique_list:
			unique_list.append(element.lower())
	return unique_list

result = unique_list(["Hallo", "hallo", "Welt", "welt"])
print(result)
"""

# c) Erweitern Sie Aufgabe b um eine Benutzereingabe bei der der Benutzer nach einer wörterliste gefragt wird und im die bereinigte Liste dann zurückgegeben wird.
"""
def unique_list(list_with_duplicated_elements):
	unique_list = []
	for element in list_with_duplicated_elements:
		if element.lower() not in unique_list:
			unique_list.append(element.lower())
	return unique_list

input_list = []
result = input("Please enter a list of elements: ")
result = result.replace('[', '')
result = result.replace(']', '')


for element in result.split(','):
	element = element.replace("'", '')
	element = element.replace('"', '')
	element = element.strip()
	input_list.append(element)

result = unique_list(input_list)
print(result)
"""