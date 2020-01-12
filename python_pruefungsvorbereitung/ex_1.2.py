# a) Fragen Sie den Benutzer nach einer Zahl. Geben Sie dann zurück, ob diese Zahl gerade oder ungerade ist.


number = int(input("Please enter a number: "))
result = "odd"
if number % 2 == 0:
	result = "even"

print("The number", number, "is", result)


# b) Geben Sie eine andere Nachricht aus, falls die Zahl ein Vielfaches von 4 ist

"""
number = int(input("Please enter a number: "))
result = "odd"
if number % 2 == 0:
	result = "even"

if number % 4 == 0:
	print("The number", number, "is a fraction of 4")

print("The number", number, "is", result)
"""