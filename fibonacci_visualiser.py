import turtle
import math

# Setup Turtle
wn = turtle.Screen()
wn.setup(1000, 800)
myTurtle = turtle.Turtle()
myTurtle.pensize(3)

# Define a list of colors for the squares
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

def main():
    valueOne = 0
    valueTwo = 1
    fib = 1
    for i in range(8):  # Number of squares to draw
        myTurtle.color(colors[i % len(colors)])  # Set color for each square
        myTurtle.right(90)  # Point turtle to down position
        drawSq(fib * 20)  # Call drawSq function - argument = length of sides
        displayFibNumber(fib, fib * 20)  # Display Fibonacci number in the square
        fib = valueOne + valueTwo  # Calculate the value of Fibonacci
        valueOne = valueTwo
        valueTwo = fib

# Function to draw the Fibonacci square
def drawSq(sides):
    for n in range(4):  # Correct to 4 for proper square drawing
        myTurtle.forward(sides)  # Draw the sides of the squares
        myTurtle.left(90)  # Turn pointer left 90 degrees

# Function to display Fibonacci numbers
def displayFibNumber(fib, size):
    myTurtle.penup()
    myTurtle.forward(size / 2)  # Move to center of the square
    myTurtle.right(90)
    myTurtle.forward(size / 2)  # Move to center of the square
    myTurtle.pendown()
    myTurtle.color("black")  # Set color for text
    myTurtle.write(fib, align="center", font=("Arial", 12, "normal"))  # Write Fibonacci number
    myTurtle.penup()
    myTurtle.left(90)
    myTurtle.backward(size / 2)  # Move back to starting position
    myTurtle.backward(size / 2)  # Move back to starting position
    myTurtle.pendown()

def sprial():
    myTurtle.right(90)  # Turn turtle to down position
    myTurtle.penup()
    myTurtle.setpos(0, 0)  # Move turtle to starting point of first square
    myTurtle.pendown()
    
    # Draw Fibonacci spiral using the Fibonacci sequence
    fib_sequence = [1, 1, 2, 3, 5, 8, 13, 21]  # Fibonacci numbers
    for fib in fib_sequence:
        arc(fib * 20, 90)  # Call arc function with Fibonacci length

def arcLine(n, length, angle):  # Draws n line segments
    for i in range(n):
        myTurtle.forward(length)
        myTurtle.left(angle)

def arc(r, angle):  # Draws an arc with the given radius and angle
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    myTurtle.left(step_angle / 2)
    arcLine(n, step_length, step_angle)
    myTurtle.right(step_angle / 2)

# Main program loop
main()  # Calls the main function which draws the boxes
sprial()  # Calls the spiral function which draws the spiral
wn.exitonclick()  # Click on the screen to exit the program
