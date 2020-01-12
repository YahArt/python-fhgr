# a) Nehmen Sie eine Liste mit Zahlen. Schreiben Sie ein Programm, dass alle Zahlen aus dieser Liste ausgibt, die kleiner 5 sind

number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for numer in number_list:
	if number < 5:
		print(number)

# b) Anstatt die Zahlen einzeln auszugeben, erstellen Sie eine neue Liste mit den Zahlen kleiner 5 und geben Sie die gesammte Liste aus.

"""
number_list = []
for number in range(5):
	number_list.append(number)

print(number_list)
"""

# c) Fragen Sie den Benutzer nach einer Zahl und geben Sie dann nur die Zahlen von der Liste aus, die kleiner als die angegebene Zahl ist.

"""
number_list = []

upper_limit = int(input("Please enter an upper limit: "))


for number in range(upper_limit):
	number_list.append(number)

print(number_list)
"""

# d) Fragen Sie den Benutzer nach einer Zahl und dannach, ob die Zahlen ausgegeben werden sollen die grösser oder kleiner als der eingebenen Zahl sind.

"""
number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number_to_compare = int(input("Please enter a number for comparison: "))
comparison_operator = input("Please enter '<' or '>': ")

for number in number_list:
	if comparison_operator == '<':
		if number < number_to_compare:
			print(number)
	else:
		if number > number_to_compare:
			print(number)
"""