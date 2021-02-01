import turtle

t = turtle.Turtle()
t.pensize(2)
t.color('white','red')
t.speed(100)
t.begin_fill()
for i in range(100):
    t.circle(10+i,45)
t.end_fill()
turtle.mainloop()
