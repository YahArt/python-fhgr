import turtle

def quadrat():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)


turtle.pensize(5)
turtle.color("red")

turtle.fillcolor("magenta")
turtle.begin_fill()
quadrat()
turtle.end_fill()

turtle.right(72)
turtle.fillcolor("yellow")
turtle.begin_fill()
quadrat()
turtle.end_fill()

turtle.right(72)
turtle.fillcolor("cyan")
turtle.begin_fill()
quadrat()
turtle.end_fill()

turtle.right(72)
turtle.fillcolor("green")
turtle.begin_fill()
quadrat()
turtle.end_fill()

turtle.right(72)
turtle.fillcolor("blue")
turtle.begin_fill()
quadrat()
turtle.end_fill()



turtle.exitonclick()
