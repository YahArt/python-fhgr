# 1.2
glossar = {
    "Begriff_1": "Wert_1",
    "Begriff_2": "Wert_2",
}

# As an alternative pprint could be used
for key in glossar:
    print(key, ":", glossar[key])

term = input("Please enter a term you want to know more about: ")
if not glossar.get(term):
    print("Sorry the term", term, "does not exist")
else:
    print("Here's the definition for the term", term, ":", glossar[term])
