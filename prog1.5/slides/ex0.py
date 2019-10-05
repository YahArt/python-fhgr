def berechne_taxi_preis(tageszeit, distanz):

    # Wir nehmen an es ist Nacht
    start_preis = 10
    preis_pro_kilometer = 4

    if tageszeit == "Tag":
        start_preis = 8
        preis_pro_kilometer = 3

    # Die ersten zwei Kilometer sind gratis
    distanz = distanz - 2
    if distanz <= 0:
        print("Der Preis in der Tageszeit", tageszeit,  "beträgt", start_preis)
    else:
        preis = start_preis + distanz * preis_pro_kilometer
        print("Der Preis in der Tageszeit", tageszeit, "mit der Distanz", distanz, "km beträgt", preis)

tageszeit = input("Tageszeit ('Tag' oder 'Nacht'): ")
distanz = int(input("Die Strecke in Kilometer: "))
berechne_taxi_preis(tageszeit, distanz)
