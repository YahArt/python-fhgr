# Schreiben Sie ein Programm, dass den Benutzer nach einer Zahl fragt und dann alle Zahlen zurückgibt, dass durch die die Zahl ohne Rest dividiert werden kann.

number = int(input("Please enter a number: "))

for i in range(1, number + 1):
	if number % i == 0:
		print(i)
