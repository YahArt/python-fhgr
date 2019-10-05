# Save some friends in a list
my_friends = []
my_friends.append("friend 1")
my_friends.append("friend 2")
my_friends.append("friend 3")
my_friends.append("friend 4")


def grüsse(index):
    # Safety check the index it cannot be less then 0 and more then the number of elements in the list
    if index < 0 or index > len(my_friends) - 1:
        print("Diese Person existiert nicht...")
    else:
        print("Hallo", my_friends[index])

grüsse(3)