# a
dict_a = [
    {
        "name": "Max Muster",
        "nummer": "30493094"
    },
    {
        "name": "Sonja Muster",
        "nummer": "30493094"
    },
    {
        "name": "Sora Muster",
        "nummer": "30493094"
    },
]

# We would be able to access the first person like this...
print(dict_a[0]["name"])

# b
dict_b = [
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

# c
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
person = search_person(dict_b, name)
if person:
    print("The following person was found:", person)
else:
    print("No person with the name", name, "exists...")
