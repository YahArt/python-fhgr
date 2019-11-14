def check_range(number, min_max_list):
    min = min_max_list[0]
    max = min_max_list[1]
    return number >= min and number <= max

notrity_level_map = {
    "Forever Alone": [-1, -9999],
    "Neutral": [0, 399],
    "Accepted": [1000, 1999],
    "Liked": [2000, 3999],
    "Trusted": [4000, 7999],
}

punkte = int(input("Bitte gib deine Punktzahl ein: "))
for key in notrity_level_map:
    range = notrity_level_map[key]
    is_in_range = check_range(punkte, range)
    if is_in_range:
        print(key)
