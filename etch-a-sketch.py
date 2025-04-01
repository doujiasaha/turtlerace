from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

north = 90

def move_forwards():
    tim.forward(30)

def turn_right():
    tim.right(30)
    
def turn_left():
    tim.left(30)
    
def move_backwards():
    tim.back(30)
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    tim.seth(90)   

tim.seth(90)


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()