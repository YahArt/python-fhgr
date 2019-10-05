import turtle

def buchstabe_y():
    # Der Rahmen der uns für das Zeichnen unseres Buchstaben zur Verfügung steht...
    rahmen_breite = 300
    rahmen_hoehe= 400

    # Ein paar Farben welche wir für die Quadrate des Hintergrunds benutzen, weitere Farben können folgender URL entnommen werden: https://ecsdtech.com/8-pages/121-python-turtle-colors?source=post_page-----52cb0939d125----------------------
    quadrat_farben = ["#E8E2DB", "#1A3263"]

    # Die Breite eines einzelnen Quadrates unsereres Hintergunds
    quadrat_breite = 100

    # Wir merken uns zuerst mal unsere aktuelle start position in x und y um einfach wieder zurückkehren zu können
    start_x = turtle.xcor()
    start_y = turtle.ycor()


    # Diese Variablen definieren das Aussehen unseres "Y"
    strich_dicke = 10
    text_groesse = 196
    font = "Arial"
    fuell_farbe_y = "#F5564E"
    schatten_farbe_y = "#FAB95B"
    text_stil = "bold" # kursiv

    # Die Position bei welcher wir beginnen das "Y" zu zeichnen.
    x_position_y_zeichnung = start_x + (rahmen_breite - text_groesse) * 0.5
    y_position_y_zeichnung = start_y + (rahmen_hoehe - text_groesse) * 0.3


    def zeichne_rechteck(breite, hoehe, fuell_farbe, rahmen_breite = 1):
        turtle.pensize(rahmen_breite)
        turtle.fillcolor(fuell_farbe)
        turtle.begin_fill()
        turtle.forward(breite)
        turtle.left(90)
        turtle.forward(hoehe)
        turtle.left(90)
        turtle.forward(breite)
        turtle.left(90)
        turtle.forward(hoehe)
        turtle.end_fill()

        # Hiermit stellen wir sicher, dass wir wieder nach "Rechts" ausgerichtet sind...
        turtle.left(90)

    def zeichne_rechteck_mit_dreiecken(breite, hoehe, farben, rahmen_breite = 1):
        # Wir extrahieren die Farben der zwei Dreiecke, aus welches unser Rechteck besteht...
        erste_farbe = farben[0]
        zweite_farbe = farben[1]

        # Wir benutzen den Satz des Pytagoras um die Hypotenuse unseres Rechtecks zu berechnen...
        hypothesen_laenge = (breite * breite + hoehe * hoehe) ** 0.5

        turtle.pensize(rahmen_breite)

        # Unser erstes Dreieck
        turtle.fillcolor(erste_farbe)
        turtle.begin_fill()
        turtle.forward(breite)
        turtle.left(90)
        turtle.forward(hoehe)
        turtle.left(135)
        turtle.forward(hypothesen_laenge)
        turtle.right(135)
        turtle.end_fill()

        # Unser zweites Dreieck
        turtle.fillcolor(zweite_farbe)
        turtle.begin_fill()
        turtle.forward(hoehe)
        turtle.right(90)
        turtle.forward(breite)
        turtle.right(135)
        turtle.forward(hypothesen_laenge)
        turtle.left(135)
        turtle.end_fill()

    def relative_bewegung_ohne_zu_zeichnen(x_offset, y_offset):
        # Zuerst merken wir uns unsere jetzige Position
        aktuelles_x = turtle.xcor()
        aktuelles_y = turtle.ycor()

        turtle.penup()
        turtle.setx(aktuelles_x + x_offset)
        turtle.sety(aktuelles_y + y_offset)
        turtle.pendown()

    def absolute_bewegung_ohne_zu_zeichnen(x, y):
        turtle.penup()
        turtle.setx(x)
        turtle.sety(y)
        turtle.pendown()

    def zeichne_hintergrund():
        # Wir merken uns unsere jetzige Position um danach wieder zurückkehren zu können...
        start_x = turtle.xcor()
        start_y = turtle.ycor()

        # Wir füllen den Hintergrund mit einem Muster aus Quadraten...
        for y in range(quadrat_breite, rahmen_hoehe + quadrat_breite, quadrat_breite):
            for x in range(0, rahmen_breite, quadrat_breite):
                zeichne_rechteck_mit_dreiecken(quadrat_breite, quadrat_breite, quadrat_farben)
                # Bewege dich zur Positon für das nächste Quadrat
                relative_bewegung_ohne_zu_zeichnen(quadrat_breite, 0)

            # Kehre zur Ausgangsposition zurück um die nächste "Reihe" zu zeichnen....
            absolute_bewegung_ohne_zu_zeichnen(start_x, y)

        # Kehre zur Startposition for dem eigentlichen Zeichnen zurück...
        absolute_bewegung_ohne_zu_zeichnen(start_x, start_y)

    def zeichne_cooles_y(x, y, farbe, strich_dicke, text_groesse, font):

        absolute_bewegung_ohne_zu_zeichnen(x, y)

        turtle.pensize(strich_dicke)
        turtle.pencolor(farbe)

        # Turtle erlaubt es uns auch Buchstaben mit Hilfe einer Font zu zeichnen (https://stackoverflow.com/questions/15141031/python-turtle-draw-text-with-on-screen-with-larger-font) :)
        turtle.write("Y", font=(font, text_groesse, text_stil))


    # Hier beginnt nun unsere eigentliche Arbeit...
    zeichne_rechteck(rahmen_breite, rahmen_hoehe, "white", 5)


    # Wir beschleunigen das Zeichnen des Hintergrunds ein wenig :)
    turtle.speed("fastest")
    zeichne_hintergrund()

    # Wir setzen die Geschwindigkeit wieder auf ein normales Niveau zurück
    turtle.speed("normal")

    # Wir zeichnen unser eigentliches Y. Dies machen wir zweimal leicht versetzt mit unterschiedlichen Farben um ein "Schatteneffekt" zu erzeugen :)
    for i in range(2):
        # Die eigentliche Füllfarbe des Y
        farbe = fuell_farbe_y
        if i % 2 == 0:
            # Die Schattenfarbe
            farbe = schatten_farbe_y

        # Wir definiere einen Offset um einen Schatteneffekt zu bekommmen...
        x = x_position_y_zeichnung + (i* 9)
        y = y_position_y_zeichnung
        zeichne_cooles_y(x, y, farbe, strich_dicke, text_groesse, font)


    # Wir stellen sicher, dass wir an der korrekten Endposition sind...
    absolute_bewegung_ohne_zu_zeichnen(start_x + rahmen_breite, start_y)

    # Wir setzen Füllfarbe etc. zurück
    turtle.pencolor("black")
    turtle.fillcolor("white")
    turtle.pensize(1)


# Zeit unser Y zu zeichnen :)
buchstabe_y()
turtle.exitonclick()
