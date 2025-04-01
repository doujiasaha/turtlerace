from turtle import Turtle, Screen
import random

#main class
class New_turtle():
    def __init__(self, id):
        self.id = id   
        #possible colors
        color = ["red","blue","green","yellow","black","pink",]
        
        self.turtle = Turtle()
        self.turtle.color(color[self.id])
        self.turtle.shape("turtle")
        self.turtle.penup()
        
        self.starting_position()
    
        
    def starting_position(self):
        
        y_positions = [-150,-100,-50,0,50,100]
        self.turtle.goto(x=-230,y=y_positions[self.id])    
       

screen = Screen()
screen.title("Welcome to the turtlerace!")
screen.setup(width=500, height=400)

user_bet = screen.textinput("Which turtle will win?", prompt="The candidates are: red, blue, green, yellow, black, pink")
objects = [New_turtle(i) for i in range(6)]

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in objects:
        if turtle.turtle.xcor() > 230:
            winning_color = turtle.turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print("You've won")
            else:
                print(f"The winning turtle was {winning_color}")
            break
        turtle.turtle.forward(random.randint(1,20))
        



        
screen.exitonclick()
