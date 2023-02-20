import turtle
import random

# define leaves of tree
def tree(d, s):
    if d <= 0:
        return
    turtle.forward(s)
    tree(d-1,s*0.8)
    turtle.right(120)
    tree(d-3,s*0.5)
    turtle.right(120)
    tree(d-3,s*0.5)
    turtle.right(120)
    turtle.backward(s)

n = 100
turtle.speed("fastest") # set speed

turtle.left(90)
turtle.forward(3 * n)
turtle.color("orange", "yellow")
turtle.left(126)

turtle.begin_fill()
for i in range(5):
    turtle.forward(n / 5)
    turtle.right(144)
    turtle.forward(n / 5)
    turtle.left(72)

turtle.end_fill()
turtle.right(126)
turtle.color("dark green")
turtle.backward(n * 4.8)

# run method
tree(15, n)
turtle.backward(n / 5)

turtle.mainloop()

# add Christmas lights
# turtle.pensize(5)
# for i in range(50):
#     x = random.randint(-300, 300)
#     y = random.randint(-100, 200)
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     colors = ["yellow", "green", "red"]
#     turtle.dot(10, random.choice(colors))
    
# turtle.done()
