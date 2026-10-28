# Daven Striedinger
# September 1, 2026
# P4LAB1
# This program uses turtle graphics, a while loop, and a for loop 
# to draw a house consisting of a square base and a triangular roof, 
# with customized window background and turtle colors.

# PSEUDOCODE:
# 1. Import the turtle module.
# 2. Setup the screen / window background color.
# 3. Create a turtle object and set its color and pen properties.
# 4. Use a while loop to draw the 4 sides of the square base:
#    a. Move forward a set distance (e.g., 100 pixels).
#    b. Turn 90 degrees right.
#    c. Increment the loop counter.
# 5. Reposition the turtle to the top-right corner of the square to start the roof.
# 6. Use a for loop to draw the 3 sides of the triangle roof:
#    a. Move forward 100 pixels.
#    b. Turn 120 degrees left (or right depending on orientation).
# 7. Complete the drawing and keep the turtle window open until clicked.

import turtle

def main():
    # Setup screen and turtle
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    
    t = turtle.Turtle()
    t.pensize(3)
    t.color("darkgreen")
    t.speed(3)
    
    # Draw the square base using a while loop
    side_count = 0
    while side_count < 4:
        t.forward(100)
        t.right(90)
        side_count = side_count + 1
        
    # Reposition turtle to top-left of square to align the roof
    t.penup()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.pendown()
    
    # Optional: fill the roof triangle for a nice look like the example
    t.fillcolor("green")
    t.begin_fill()
    
    # Draw the triangle roof using a for loop
    for i in range(3):
        t.forward(100)
        t.left(120)
        
    t.end_fill()
    
    # Hide turtle and keep window open
    t.hideturtle()
    turtle.done()

if __name__ == '__main__':
    main()