import turtle

def square(t,l):
    for i in range(4):
        t.fd(l)
        t.lt(90)
        
t = turtle.Turtle()
t.pensize(2)
t.color('red','blue')
l = int(input('Enter length : '))
t.begin_fill()
square(t,l)
t.end_fill()
turtle.mainloop()
