# d
telephone_book = {
    "Max": {
        "Name": "Max Muster",
        "Nummer": "656262",
        "Strasse": "Musterstrasse",
        "Hausnummer": "8",
        "Stadt": "Mels",

    },
    "Helene": {
        "Name": "Helene Muster",
        "Nummer": "656262",
        "Strasse": "Musterstrasse",
        "Hausnummer": "15",
        "Stadt": "Mels",

    },
}

# c
name = input("Please enter the name of the person you want to know more about: ")
property = input("Please enter the field you want to know more about: ")
if not telephone_book.get(name):
    print("The person with the name", name, "does not exist")
else:
    if not telephone_book[name].get(property):
        print("The field", property, "does not exist on this person")
    else:
        print(telephone_book[name][property])
