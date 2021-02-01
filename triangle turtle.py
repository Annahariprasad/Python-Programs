import turtle

def triangle(t):
    for i in range(3):
        t.fd(100)
        t.lt(120)
        
t = turtle.Turtle()
t.color('red','blue')
t.begin_fill()
triangle(t)
t.end_fill()
turtle.mainloop()
