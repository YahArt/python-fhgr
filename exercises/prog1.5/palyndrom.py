def ist_palyndrom(wort):
    if wort.lower() == wort[::-1].lower():
        print("Das Wort", wort, "ist ein Palyndrom")
    else:
        print("Das Wort", wort, "ist kein Palyndrom")



wort = input("Bitte geben Sie ein Wort ein: ")
ist_palyndrom(wort)
