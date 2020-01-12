import random

# a) Schreiben Sie ein Programm, dass eine zufällige Zahl zwischen 1 und 10 generiert und dann denn Benutzer raten lässt, um welche Zahl es sich handelt.
lower = int(input("Please enter a number for the lower bound: "))
upper = int(input("Please enter a number for the upper bound: "))

secret = random.randint(lower, upper)

guess = int(input("Please enter your guess: "))

while guess != secret:
	print("Your guess", guess, "was wrong")
	if guess < secret:
		print("It was to low")
	else:
		print("It was to high")
	guess = int(input("Please enter your guess: "))

print("Your guess", guess, "was correct")


#b) Erweitern sie das Programm, sodass es zum Schluss ausgibt, wie oft der Benutzer falsch geraten hat.
"""
lower = int(input("Please enter a number for the lower bound: "))
upper = int(input("Please enter a number for the upper bound: "))

secret = random.randint(lower, upper)
number_of_wrong_guesses = 0

guess = int(input("Please enter your guess: "))

while guess != secret:
	print("Your guess", guess, "was wrong")
	number_of_wrong_guesses += 1
	if guess < secret:
		print("It was to low")
	else:
		numb
		print("It was to high")
	guess = int(input("Please enter your guess: "))

print("Your guess", guess, "was correct")
print("You had", number_of_wrong_guesses, "wrong guesses.")
"""