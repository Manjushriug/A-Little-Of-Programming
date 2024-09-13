import turtle

pen = turtle.Turtle()

# Input: Ask the user for a distance and angle
distance = int(input("How far should the turtle move forward? "))
angle = int(input("What angle should the turtle turn (0 to 360 degrees)? "))

# Output: Move the turtle and turn it based on the input
pen.forward(distance)   # Move forward
pen.right(angle)        # Turn the turtle by the angle

# Output: Move again to see the turtle's new direction
pen.forward(distance)

turtle.done()
