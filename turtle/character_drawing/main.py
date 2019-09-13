import turtle
import math # Needed for sqrt 

def draw_y():
    # The border
    border_width = 300
    border_height = 400

    # Colors are defined here: https://ecsdtech.com/8-pages/121-python-turtle-colors?source=post_page-----52cb0939d125----------------------
    # These are the two colors we use to color in our squares (which are made up of two triangles)
    square_colors = ["Lavender", "Lavender Blush"]

    # The background is filed with squares we define the widht and height here, note that this should be a number which border_width and border_height are divisible by
    square_width = 50

    # Save x and y position here so that we can get easily to the specified end point
    start_x = turtle.xcor()
    start_y = turtle.ycor()

    # The y drawing start position
    x_pos_for_y_drawing = start_x + 95
    y_pos_for_y_drawing = start_y + 50

    def draw_rectangle(width, height, fill_color, border_thickness = 1):
        turtle.pensize(border_thickness)
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.end_fill()

        # Make sure we are facing right again
        turtle.left(90)

    def draw_rectangle_with_triangles(width, height, colors, border_thickness = 1):
        # We specify two colors inside a list one for each triangle
        first_color = colors[0]
        second_color = colors[1]

        # Calculate the hypothese by pythagoras (we know the width and height) 
        hypothese_length = math.sqrt(width * width + height * height)

        turtle.pensize(border_thickness)

        # Draw first triangle and color it in
        turtle.fillcolor(first_color)
        turtle.begin_fill()
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(135)
        turtle.forward(hypothese_length)
        turtle.right(135)
        turtle.end_fill()

        # Draw the second triangle and color it in
        turtle.fillcolor(second_color)

        turtle.begin_fill()
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(135)
        turtle.forward(hypothese_length)
        turtle.left(135)
        turtle.end_fill()

        # Now we are facing right again at the bottom left

    def move_relative_without_drawing(x_diff, y_diff):
        # Get current position which we are right now.
        curr_x = turtle.xcor()
        curr_y = turtle.ycor()

        turtle.penup()
        turtle.setx(curr_x + x_diff)
        turtle.sety(curr_y + y_diff)
        turtle.pendown()

    def move_absolute_without_drawing(x, y):
        turtle.penup()
        turtle.setx(x)
        turtle.sety(y)
        turtle.pendown()

    def fill_background():
        # First we save the start x and y pos in order to return to it easily
        start_x = turtle.xcor()
        start_y = turtle.ycor()

        # Note that we do not want to start at 0 for the y but the square_width and therefore we need to adust the end step accordingly...
        for y in range(square_width, border_height + square_width, square_width):
            for x in range(0, border_width, square_width):
                draw_rectangle_with_triangles(square_width, square_width, square_colors)
                # Move by square width in order to draw the next square
                move_relative_without_drawing(square_width, 0)

            # Return to starting position and move up on each iteration
            move_absolute_without_drawing(start_x, y)

        # Make sure we are where we started before drawing this background again
        move_absolute_without_drawing(start_x, start_y)

    def draw_fancy_y(x, y, fill_color, border_color = "black", border_thickness = 1):

        move_absolute_without_drawing(x, y)

        turtle.pensize(border_thickness)
        turtle.pencolor(border_color)
        turtle.fillcolor(fill_color)
        turtle.begin_fill()

        turtle.left(90)
        turtle.forward(200)
        turtle.left(45)
        turtle.forward(130)
        turtle.right(135)
        turtle.forward(50)
        turtle.right(45)
        turtle.forward(130)
        turtle.left(90)
        turtle.forward(130)
        turtle.right(45)
        turtle.forward(50)
        turtle.right(135)
        turtle.forward(130)
        turtle.left(45)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)

        turtle.end_fill()

        # Make sure we are facing right again
        turtle.right(180)



    # The main bulk of the work starts here
    draw_rectangle(border_width, border_height, "Lemon Chiffon", 5)

    # Speed this up as this takes a little bit of time :)
    turtle.speed(10)
    fill_background()

    # Well we are done return to a more normal speed again
    turtle.speed(5)

    # Draw the actual 'Y' we do this in two times in order to create a nice shadow effect :)
    for i in range(2):
        # The foregound color
        color = "Indian Red"
        if i % 2 == 0:
            # The shadow color
            color = "Rosy Brown"

        # The apply some random offset to x in order to shift while drawing
        x = x_pos_for_y_drawing + (i* 9)
        y = y_pos_for_y_drawing
        draw_fancy_y(x, y, color, color, 0)

    # Go to the specified end point
    move_absolute_without_drawing(start_x + border_width, start_y)

    # Reset fill color border color and pen size
    turtle.pencolor("black")
    turtle.fillcolor("white")
    turtle.pensize(1)

# Let the drawing begin...
draw_y()
turtle.exitonclick()
