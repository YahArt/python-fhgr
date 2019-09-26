# d
dict_d = [
    {
        "name": "Max Muster",
        "nummer": "30493094",
        "strasse": "Strasse 1",
        "plz": "8887"
    },
    {
        "name": "Sonja Muster",
        "nummer": "30493094",
        "strasse": "Strasse 2",
        "plz": "8887"
    },
    {
        "name": "Sora Muster",
        "nummer": "30493094",
        "strasse": "Strasse 3",
        "plz": "8887"
    },
]

def search_person(dict, name):
    """This methods gets the data entry out of a dictionary with the given name"""
    # First lets find the dictionary entry with the given name in the list
    # Remember our dict is actually a list wich contains dictionaries as entires
    for person_entry in dict:
        # Check if the name is matching
        if person_entry["name"] == name:
            return person_entry

    # In case we have found nothing we just return an empty dictionary
    return {}

# Lets try that out...
name = input("Please enter the name of a person to search for: ")
wanted_field = input("Please enter the field you want to print: ")
person = search_person(dict_d, name)

# We safe check if the field actually exists in this dictionary...
key_exists = person.get(wanted_field)

# Only if the person and the wanted field inside the person exists we inform the user...
if person and key_exists:
    # We only print out the wanted field by accessing it in person
    print("The following person was found:", person[wanted_field])
else:
    print("No person with the name", name, "exists...")
