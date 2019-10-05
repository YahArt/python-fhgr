import turtle

def dreieck():
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)


turtle.pensize(5)
turtle.color("red")
turtle.left(30)

turtle.fillcolor("yellow")
turtle.begin_fill()
dreieck()
turtle.end_fill()

turtle.forward(100)
turtle.fillcolor("green")
turtle.begin_fill()
dreieck()
turtle.end_fill()

# Move to correct position for bottom triangle
turtle.right(120)
turtle.forward(100)
turtle.left(120)

turtle.fillcolor("cyan")
turtle.begin_fill()
dreieck()
turtle.end_fill()

turtle.exitonclick()
