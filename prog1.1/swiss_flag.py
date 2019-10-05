import turtle

def reset_colors():
    turtle.color("black")
    turtle.fillcolor("white")

def draw_rectangle(width, height, color, fill_color):
    """ This method draws a rectangle note that we assume the turtle is facing right at the bottom left when starting """
    turtle.fillcolor(fill_color)
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90) # make the turtle face right again
    turtle.end_fill()

    reset_colors()

def move_relative(x, y):
    """ This method allows relative movement of the turtle without drawing """
    curr_x = turtle.xcor()
    curr_y = turtle.ycor()

    turtle.penup()
    turtle.setx(curr_x + x)
    turtle.sety(curr_y + y)
    turtle.pendown()

def draw_swiss_cross(side_width, color, fill_color):
    """ This method draws the swiss cross the side with defines the width of a single 'square' of the swiss cross """

    # Note that we could use some kind of loop but I think this is more straight forward to read :)
    turtle.color(color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    
    # Bottom
    turtle.forward(side_width)
    turtle.right(90)
    turtle.forward(side_width)
    turtle.left(90)
    turtle.forward(side_width)
    turtle.left(90)
    turtle.forward(side_width)
    turtle.right(90)
    
    # Right
    turtle.forward(side_width)
    turtle.left(90)
    turtle.forward(side_width)
    turtle.left(90)
    turtle.forward(side_width)
    turtle.right(90)

    # Top
    turtle.forward(side_width)
    turtle.left(90)
    turtle.forward(side_width)
    turtle.left(90)
    turtle.forward(side_width)
    turtle.right(90)

    # Left
    turtle.forward(side_width)
    turtle.left(90)
    turtle.forward(side_width)
    turtle.left(90)
    turtle.end_fill()

    reset_colors()

swiss_flag_size = int(input("Please enter a size for the swiss flag: "))

# Deactivate the arrow / turtle
turtle.hideturtle()

# Calculate the segment width as a percentage depending on the swiss flag size
swiss_cross_segment_width = swiss_flag_size * 0.2
draw_rectangle(swiss_flag_size, swiss_flag_size, "red", "red")

# Calculate where we would need to move in order to draw the swiss cross horizontally and vertically centered.
# Here we calculate the position of the left swiss cross segment so that we can start drawing from there
# The calculation is not to difficult as we know the swiss cross has a total of 3 'squares'
start_x = (swiss_flag_size - 3 * swiss_cross_segment_width) * 0.5
start_y = ((swiss_flag_size - 3 * swiss_cross_segment_width) * 0.5) + swiss_cross_segment_width

move_relative(start_x, start_y)
draw_swiss_cross(swiss_cross_segment_width, "white", "white")
turtle.exitonclick()