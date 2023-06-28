from turtle import Turtle, Screen, colormode
import random
 
colour_list = [(239, 236, 238), (239, 237, 235), (236, 237, 242), (228, 238, 231), (28, 107, 162),]
 
colormode(255)
 
turtle = Turtle()
turtle.shape("turtle")
turtle.color("maroon")
turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()
 
start_pos_x = -240
start_pos_y = -220
 
turtle.setpos(start_pos_x, start_pos_y)
 
 
def paint(width, height, gap):
    for i in range(height):
        for _ in range(width):
            turtle.dot(20, random.choice(color_list))
            turtle.forward(50)
        turtle.setpos(start_pos_x, turtle.pos()[1] + gap)
 
 
paint(10, 10, 50)
 
screen = Screen()
screen.title("Hirst Painting")
screen.exitonclick()
