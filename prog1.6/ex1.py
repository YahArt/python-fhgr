# Exercise 3.2

"""
We use the english word as a key because that is what the user is entering.
We will also enter these lower case which makes them easier to find because we will lower case the user input also
Because I find the names from 9gag halerious we will use those for more information see https://9gag.com/gag/am8OoA9/funny-animal-names
"""
vocabulary_9gag = {
    "fart squirrel": "Stinktier",
    "danger floof": "Bär",
    "sea flap flap": "Manta Rochen",
    "treefloof majestic": "Koalabär",
    "giraffe sheep": "Lahma",
    "trash panda": "Waschbär",
    "sea catsnake": "Otter",
    "spiky floof": "Igel",
}

score = 0

# Well let's get this pary started
print("Welcome to the 9gag vocabulary test let's see what you got...")
for key, value in vocabulary_9gag.items():
    english_word = input("What does '" +  value + "' translate to: ")

    # Let's check if his guess was correct we also do a lower here to ignore the way the user enters his guess (FART squirrel and fart squirrel are the same)
    if english_word.lower() == key:
        print("CORRECT")
        score += 1
    else:
        print("WRONG!")

print("Alrighty let's see your results...")
print("You got", score, "out of", len(vocabulary_9gag.keys()), "correct")
