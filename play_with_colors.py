import turtle

pen = turtle.Turtle()

# Input: Ask for a color
color = input("What color should the turtle draw with? ")

# Change the pen color
pen.color(color)

# Output: Draw a square in the chosen color
for _ in 4:
    pen.forward(100)
    pen.right(90)

turtle.done()
