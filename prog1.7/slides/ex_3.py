from pprint import pprint # For priting out the dictionary nicely...
from json import loads, dumps # For saving and loading to JSON.

# The inital persons in the telephone book
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

def print_telephone_book():
    pprint(telephone_book)


def save_to_json():
        file_name = input("Please enter a file name: ")
        try:
            with open(file_name, 'w', encoding='utf-8') as json_file:
                content = dumps(telephone_book)
                json_file.write(content)
                print("Saved successfully to", file_name)
        except Exception:
            print("Something went wrong with trying to save the data to", file_name)

def load_from_json():
    file_name = input("Please enter a file name: ")
    try:
        with open(file_name, 'r', encoding='utf-8') as json_file:
            content = json_file.read()

            # Restore the telephone book data structure
            print("Successfully restored the telephone book from file", file_name)
            return loads(content)

    except Exception:
        print("Something went wrong with trying to load the data from", file_name)

running = True

while running:
    print("==============================================")
    print("What do you want to do:")
    print("For printing the whole telephone book 'p'")
    print("For searching press 'f'")
    print("For adding a new person press 'a'")
    print("For saving the current data as a JSON File 's'")
    print("For loading telephone book data from a JSON File 'l'")
    print("For quitting press 'q'")

    decision = input("Your anwser: ")

    if decision == 'p':
        print_telephone_book()
    elif decision == 'f':
        name = input("Enter the name of the person you want to search for: ")
        search_person(name)
    elif decision == 'a':
        add_person()
    elif decision == 's':
        save_to_json()
    elif decision == 'l':
        telephone_book = load_from_json()
    elif decision == 'q':
        print("Ok bye...")
        running = False
        break
    else:
        print("Sorry this is not a valid command...")
