# Exercise 3.1
city  = input("Please enter a city (or 'x' to quit): ")
list = list()
while city != 'x':
    population = int(input("Please enter the population: "))

    if population < 0:
        print("What do we have here... some Zombies or what? Well in that case let me get my trusty flamethrower")

    list.append([city, population])

    # Keep the loop going
    city  = input("Please enter a city (or 'x' to quit): ")

print(sorted(list))
