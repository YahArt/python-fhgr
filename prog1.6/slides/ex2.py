my_dict = {"Chur": "7000",  "Sargans": "7320",  "Bad Ragaz": "7310"}

for key, value in my_dict.items():
    print(key, "hat die", value, "als Postleitzahl")

for key in my_dict:
    print(key, "hat die", my_dict[key], "als Postleitzahl")
