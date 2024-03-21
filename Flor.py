from turtle import *
import colorsys
import math
import time

hideturtle()  # Oculta la flecha de la tortuga
speed(0.25)
bgcolor("black")

# Genera los pétalos
goto(0, -40)
h = 0

for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(0.125, 1, 1)
        color(c)
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

# Genera la parte central de la flor
color("black")
shape("turtle")  # Se oculta pero sigue siendo necesario para la operación de la tortuga
fillcolor("brown")
phi = 137.508 * (math.pi / 180.0)

for i in range(200):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()
    stamp()

# TEXTO "Flor"
penup()
goto(200, 280)  # Mueve el texto a la parte superior derecha
pendown()
color("white")
write("💕Alfredo & Quetzaly💕", align="center", font=("Courier", 18, "normal"))  # Cambia la tipografía
time.sleep(2)

done()