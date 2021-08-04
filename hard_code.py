import colorgram
import turtle
import random

my_turtle = turtle.Turtle()
turtle.colormode(255)
from turtle import Screen


def main():
    """rgb_colors = list()
    colors = colorgram.extract('image.jpg', 12)
    for color in colors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        color_3 = (red, green, blue)
        rgb_colors.append(color_3)"""
    rgb_colors=[(239, 245, 250), (236, 224, 80), (196, 8, 69), (112, 179, 215), (199, 76, 17), (230, 54, 131), (216, 162, 102), (195, 163, 15), (12, 23, 63)]
    my_turtle.penup()
    my_turtle.speed("fastest")
    my_turtle.setposition(-350,-300)
    for i in range(8):
        my_turtle.pendown()
        my_turtle.color(random.choice(rgb_colors))
        my_turtle.begin_fill()
        my_turtle.circle(13)
        my_turtle.end_fill()
        for j in range(10):
            my_turtle.penup()
            my_turtle.forward(70)
            my_turtle.pendown()
            my_turtle.color(random.choice(rgb_colors))
            my_turtle.begin_fill()
            my_turtle.circle(13)
            my_turtle.end_fill()
        my_turtle.color(random.choice(rgb_colors))
        my_turtle.penup()
        my_turtle.left(90)
        my_turtle.forward(70)
        my_turtle.left(90)
        my_turtle.pendown()
        my_turtle.begin_fill()
        my_turtle.circle(13)
        my_turtle.end_fill()
        for j in range(10):
            my_turtle.penup()
            my_turtle.forward(70)
            my_turtle.pendown()
            my_turtle.color(random.choice(rgb_colors))
            my_turtle.begin_fill()
            my_turtle.circle(13)
            my_turtle.end_fill()
        my_turtle.color(random.choice(rgb_colors))
        my_turtle.penup()
        my_turtle.right(90)
        my_turtle.forward(20)
        my_turtle.right(90)
        my_turtle.pendown()
        my_turtle.begin_fill()
        my_turtle.circle(13)
        my_turtle.end_fill()
    screen = Screen()
    print(screen.canvheight)
    print(screen.canvwidth)
    screen.exitonclick()

if __name__ == "__main__":
    main()