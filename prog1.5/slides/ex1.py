def notoriety_level(points):
    if points < 0:
        return "Forever Alone"
    elif points < 400:
        return "Neutral"
    elif points < 1000:
        return "Accepted"
    elif points < 2000:
        return "Liked"
    elif points < 4000:
        return "Trusted"
    elif points < 8000:
        return "Idolized"
    elif points < 20000:
        return "Renowned"
    else:
        return "Glorious"

points = int(input("Please enter your points: "))
print("With", points, "you have the following notoriety level:", notoriety_level(points))
