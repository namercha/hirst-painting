# Using the colorgram package to extract the top colors in an image.
# import colorgram
import turtle as t, random


# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# Using the commented code above to generate a list of colors below.
color_list = [(2, 12, 31), (53, 25, 17), (219, 127, 106), (10, 105, 159), (242, 213, 69), (149, 84, 39), (214, 87, 64),
              (164, 162, 32), (158, 6, 24), (157, 62, 102), (96, 6, 19), (11, 63, 32), (207, 73, 104), (11, 96, 56),
              (173, 135, 161), (1, 63, 146), (8, 174, 216), (158, 33, 24), (4, 212, 207), (8, 140, 86), (145, 227, 216),
              (122, 193, 148), (221, 178, 217), (101, 219, 229), (252, 196, 0), (118, 168, 190)]
tim = t.Turtle()
PENSIZE = 20
SPACING = 50
number_of_dots = 100
t.colormode(255)
tim.hideturtle()
# Setting starting position for Tim
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")


for dot_count in range(1, number_of_dots + 1):
    tim.dot(PENSIZE, random.choice(color_list))
    tim.forward(SPACING)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(SPACING)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()