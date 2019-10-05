import turtle

def quadrat(groesse):
    turtle.forward(groesse)
    turtle.left(90)
    turtle.forward(groesse)
    turtle.left(90)
    turtle.forward(groesse)
    turtle.left(90)
    turtle.forward(groesse)
    turtle.left(90)


def zeichne_blume(farbe, strich_dicke, groesse):
    turtle.pensize(strich_dicke)
    turtle.color(farbe)

    turtle.fillcolor(farbe)
    turtle.begin_fill()
    quadrat(groesse)
    turtle.end_fill()

    turtle.right(72)
    turtle.begin_fill()
    quadrat(groesse)
    turtle.end_fill()

    turtle.right(72)
    turtle.begin_fill()
    quadrat(groesse)
    turtle.end_fill()

    turtle.right(72)
    turtle.begin_fill()
    quadrat(groesse)
    turtle.end_fill()

    turtle.right(72)
    turtle.begin_fill()
    quadrat(groesse)
    turtle.end_fill()


farbe = input("Welche Farbe soll die Blume haben ('cyan', 'red', 'blue', ...): ")
strich_dicke = int(input("Welche Strichdicke soll die Blume haben: "))
groesse = int(input("Welche Grösse soll die Blume haben: "))

zeichne_blume(farbe, strich_dicke, groesse)
turtle.exitonclick()
