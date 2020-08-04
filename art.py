import turtle
w = turtle.Turtle()
step = 20
w.penup()
for i in range(30):
    
    w.forward(step)
    w.left(24)
    w.stamp()
    step = step + 3



turtle.done()