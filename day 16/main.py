import tkinter
from turtle import Turtle, Screen

timmy = Turtle()


print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
my_screen = Screen()
my_screen.canvheight = 100
print(my_screen.canvheight)
my_screen.exitonclick()