import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex
n=10
for a in range(n):
    alex.forward(40)
    alex.left(360/n)
