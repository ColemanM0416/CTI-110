#Magan Coleman
#C!S-110
#10/21/2026
#P4LAB1
#Turtle and loops to square and triangle

#Import the Library
import turtle

#Create the turtle window and draw
win= turtle.Screen()
pen = turtle.Turtle()


#Set the turtle options
pen.pensize(5)
pen.pencolor("black")
pen.shape("arrow")

#Code to draw the shape
for side in range(4):
    pen.forward(100)
    pen.right(90)

#while loop 3 times
sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1


#Wait for user to close window
win.mainloop()