# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle

turtle.colormode(255)
tim = turtle.Turtle()

tim.hideturtle()

color_list = [(207, 160, 83), (55, 89, 131), (145, 91, 40), (139, 26, 48), (222, 206, 109), (133, 176, 202),
              (157, 47, 83), (46, 55, 103), (129, 188, 143), (166, 160, 39), (83, 20, 45), (37, 42, 68), (185, 94, 106),
              (187, 140, 170), (38, 25, 19), (85, 124, 181), (79, 153, 164), (88, 157, 91), (193, 78, 73), (45, 74, 77),
              (161, 201, 219), (80, 73, 43), (55, 132, 129), (218, 176, 187), (220, 183, 166), (169, 206, 169)
              ]
matrix_size = int(input('How many rows and columns do you want?: '))
diameter = int(input('How much diameter do you want?: '))
radius = int(diameter / 2)
tim.penup()
x = int((matrix_size * 2 + 1) * radius / 2 - radius)
y = int((matrix_size * 2 + 1) * radius / 2 - radius)
for a in range(-y, y, diameter):
    tim.sety(a)
    for b in range(-x, x, diameter):
        color = random.choice(color_list)
        tim.setx(b)
        tim.dot(radius, color)







screen = turtle.Screen()
screen.exitonclick()