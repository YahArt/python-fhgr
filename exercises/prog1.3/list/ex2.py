# Save some friends in a list
my_friends = []
my_friends.append("friend 1")
my_friends.append("friend 2")
my_friends.append("friend 3")
my_friends.append("friend 4")

# Greet them
print("Hallo", my_friends[0])
print("Hallo", my_friends[1])
print("Hallo", my_friends[2])
print("Hallo", my_friends[3])

# However we can also use a loop and make things simpler
for friend in my_friends:
    print("Hallo", friend)