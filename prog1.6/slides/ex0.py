from pprint import pprint # For priting out the dictionary nicely...

telephone_book = {
    "Max": {
        "Name": "Max Muster",
        "Nummer": "656262",
        "Strasse": "Musterstrasse",
        "Stadt": "Mels",

    },
    "Helene": {
        "Name": "Helene Muster",
        "Nummer": "656262",
        "Strasse": "Musterstrasse",
        "Stadt": "Mels",

    },
}

def add_person():
    print("Adding a new person")
    name = input("Please enter the name: ")
    number = input("Please enter the telephone number: ")
    street = input("Please enter the street: ")
    city = input("Please enter the city: ")
    telephone_book[name] = {
        "Name": name,
        "Nummer": number,
        "Strasse": street,
        "Stadt": city
    }
    pprint(telephone_book[name])

def search_person(name):
    if not telephone_book.get(name):
        print("Sorry the person with the name", name, "was not found.")
        answer = input("Do you want to add a new person (y/n): ")
        if answer == 'y':
            add_person()
        # else case does not need to be handled ad the moment...
    else:
        print("The following person was found for the name", name)
        pprint(telephone_book[name])

running = True

while running:
    print("What do you want to do:")
    print("For searching press 's'")
    print("For adding a new person press 'a'")
    print("For quitting press 'q'")

    decision = input("Your anwser: ")

    if decision == 's':
        name = input("Enter the name of the person you want to search for: ")
        search_person(name)
    elif decision == 'a':
        add_person()
    elif decision == 'q':
        print("Ok bye...")
        running = False
        break
    else:
        print("Sorry this is not a valid command...")
