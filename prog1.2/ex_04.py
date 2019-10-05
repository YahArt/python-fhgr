def berechne_bis_alter_100(momentanes_alter):
    return 100 - momentanes_alter

name = input("Bitte gib deinen Namen ein: ")
alter = int(input("Bitte gib dein Alter an: "))
anzahl_ausgabe = int(input("Wie viel mal soll die Nachricht angezeigt werden? "))
if (alter < 100):
    bis_ein_hundert = berechne_bis_alter_100(alter) + 2019
    nachricht = name + " du wirst im Jahre " + str(bis_ein_hundert) + " 100 Jahre alt sein\n"
    print(nachricht * anzahl_ausgabe)
else:
    nachricht = name + "du bist bereits 100 Jahre oder älter...\n"
    print(nachricth * anzahl_ausgabe)
