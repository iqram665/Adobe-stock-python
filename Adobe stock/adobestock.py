import turtle
import os

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")  # Premium/Dark theme-er jonno
screen.setup(width=800, height=800)

# Turtle setup
t = turtle.Turtle()
t.speed(0)  # Shobcheye druto speed
t.width(2)

# Color palette (Adobe Stock-e neon/gradient palette bhalo chole)
colors = ["#D38456", "#7B2CBF", "#B6289E", "#4361EE", "#4CC9F0"]

# Abstract Geometric Pattern Drawing
for i in range(300):
    t.pencolor(colors[i % len(colors)])
    t.forward(i * 2)
    t.right(61)  # 61 degree angle-e ekta unique spiral toiri hobe
    t.forward(i)
    t.right(120)

# Art-ti EPS format-e save korar jonno
# Eta porobortite Illustrator-e khule Vector (.AI/.EPS) banano jabe
canvas = screen.getcanvas()
canvas.postscript(file="adobe_stock_vector.eps")

print("Project complete! 'adobe_stock_vector.eps' file-ti save hoyeche.")
turtle.done()