# a) Schreiben Sie ein Programm, dass nach dem Namen und dem Alter der Person fragt und dann in einer personalisierten Mitteilung der Person mitteilt, in welchem Jahr sie 100 Jahre alt wird.


name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

until_100_years_old = 100 - age
print(name, "you will be 100 years old in", 2020 + until_100_years_old)


# b) Erweitern Sie das Programm in dem Sie den Benutzer um eine zusätzliche Zahl bitten die die Anzahl der Ausgaben der Nachricht definiert.

"""
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
number_of_repetitions = int(input("How many times should the message be repeated: "))

until_100_years_old = 100 - age

message = (name + " you will be 100 years old in " + str(2020 + until_100_years_old) + ". ") * number_of_repetitions
print(message)
"""

#c) Geben Sie die wiederholenden Ausgaben in separaten Zeilen aus.

"""
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
number_of_repetitions = int(input("How many times should the message be repeated: "))

until_100_years_old = 100 - age

for i  in range(number_of_repetitions):
	print(name, "you will be 100 years old in", 2020 + until_100_years_old)
"""