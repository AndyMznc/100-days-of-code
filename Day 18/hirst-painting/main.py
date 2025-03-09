import random
import turtle as tt

color_list = [
    (60, 215, 178),
    (97, 168, 214),
    (209, 231, 243),
    (43, 189, 164),
    (239, 226, 203),
    (216, 125, 191),
    (88, 234, 186),
    (246, 155, 217),
    (38, 127, 165),
    (187, 245, 225),
    (27, 171, 209),
    (213, 161, 96),
    (186, 89, 144),
    (133, 74, 123),
    (236, 211, 105),
    (249, 201, 222),
    (39, 139, 113),
    (147, 89, 54),
    (85, 124, 198),
    (73, 16, 30),
    (124, 24, 50),
    (128, 214, 238),
    (164, 175, 230),
    (67, 28, 18),
    (203, 147, 33),
    (231, 170, 164),
    (203, 82, 68),
    (20, 43, 71),
    (100, 46, 39),
    (47, 54, 106),
]

screen = tt.Screen()
screen.colormode(255)

pointer = tt.Turtle()
pointer.penup()
pointer.speed("fastest")
pointer.goto(-275, -275)


def painting(length):
    x_axes = pointer.xcor()
    y_axes = pointer.ycor()
    row = 1

    while row <= length:
        for _ in range(length):
            pointer.dot(20, random.choice(color_list))
            pointer.forward(50)
        if row < length:
            pointer.goto(x_axes, y_axes + 50)
            y_axes += 50
        row += 1


painting(10)

screen.exitonclick()
