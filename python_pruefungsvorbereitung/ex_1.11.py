# a) Schreiben Sie eine Funktion die ein die den Benutzer nach folgenden Daten abfrägt und diesed ann in ein dict speichert
my_dictionary = {}

def add_user(my_dictionary):
	name = input("Please enter your name: ")
	date_of_birth = input("Please enter your date of birth: ")
	city = input("Please enter your city: ")
	job = input("Please enter your job: ")

	my_dictionary = {
		'Name': name,
		'Date of Birth': date_of_birth,
		'City': city,
		'Job': job
	}

	return my_dictionary

my_dictionary = add_user(my_dictionary)
print(my_dictionary)

# b) Erweitern Sie das Programm sodass das dict formatiert ausgegeben wird.
"""
my_dictionary = {}

def add_user(my_dictionary):
	name = input("Please enter your name: ")
	date_of_birth = input("Please enter your date of birth: ")
	city = input("Please enter your city: ")
	job = input("Please enter your job: ")

	my_dictionary = {
		'Name': name,
		'Date of Birth': date_of_birth,
		'City': city,
		'Job': job
	}

	return my_dictionary

def pretty_print(my_dictionary):
	for key, value in my_dictionary.items():
		print(key, ":", value)

my_dictionary = add_user(my_dictionary)
pretty_print(my_dictionary)
"""

# c) Erweitern Sie das Programm sodass der Benutzer mehrere Datensätze eingeben kann. Nach jeder Eingabe soll der Benutzer gefragt werden, ob er einen weiteren Datensatz eingeben möchte oder ob er die Eingabe beenden möchte und die Datensätze somit ausgegeben werden sollen.
"""
my_dictionary = {}

def add_user(my_dictionary):
	name = input("Please enter your name: ")
	date_of_birth = input("Please enter your date of birth: ")
	city = input("Please enter your city: ")
	job = input("Please enter your job: ")

	my_dictionary[name] = {
		'Name': name,
		'Date of Birth': date_of_birth,
		'City': city,
		'Job': job
	}

	return my_dictionary

def pretty_print(my_dictionary):
	element = 0
	for key in my_dictionary.keys():
		element += 1
		print('_' * 5  + 'Element ' + str(element) + '_' * 5)
		for key, value in my_dictionary[key].items():
			print(key, ":", value)


answer = input("Do you want to add a new user (yes or no)? ")
while answer.lower() != 'no':
	my_dictionary = add_user(my_dictionary)
	answer = input("Do you want to add a new user (yes or no)? ")
pretty_print(my_dictionary)
"""

# d) Implementieren Sie eine Funktion, die dem Benutzer erlaubt, im Datensatz nach einer Person zu suchen um die dazugehörenden Daten zu erhalten.

"""
my_dictionary = {}

def add_user(my_dictionary):
	name = input("Please enter your name: ")
	date_of_birth = input("Please enter your date of birth: ")
	city = input("Please enter your city: ")
	job = input("Please enter your job: ")

	my_dictionary[name] = {
		'Name': name,
		'Date of Birth': date_of_birth,
		'City': city,
		'Job': job
	}

	return my_dictionary

def pretty_print(my_dictionary):
	element = 0
	for key in my_dictionary.keys():
		element += 1
		print('_' * 5  + 'Element ' + str(element) + '_' * 5)
		for key, value in my_dictionary[key].items():
			print(key, ":", value)

def get_choice():
	print("What do you want to do:")
	print("a: Add a new user")
	print("f: Search for an existing user")
	print("p: Print the dictionary")
	print("q: Quit")
	print('____________________________________')
	choice = input("Your answer: ")
	return choice.lower()

def search_for_user(my_dictionary, user_to_search_for):
	if my_dictionary.get(user_to_search_for):
		print("We have found the following information for the user", user_to_search_for)
		information = my_dictionary[user_to_search_for]
		for key, value in information.items():
			print(key, ":", value) 
	else:
		print("There is no information about the user", user_to_search_for)

choice = get_choice()
while choice != 'q':
	# Evaluate what the user wants do do
	if choice == 'a':
		my_dictionary = add_user(my_dictionary)
	elif choice == 'f':
		user_to_search_for = input("Please enter the name of the user to search for: ")
		search_for_user(my_dictionary, user_to_search_for)
	elif choice == 'p':
		pretty_print(my_dictionary)
	else:
		print('Seriously you just fucked up, try again.')
	choice = get_choice()

print('Bye')
"""