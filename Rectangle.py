import turtle

def rectangle(t,l):
    for i in range(4):
        a = t.fd(l) if(i%2 == 0) else t.fd(l/2)
        t.lt(90)

t = turtle.Turtle()
t.color('red','blue')
t.pensize(2)
l = int(input('Enter length : '))
t.begin_fill()
rectangle(t,l)
t.end_fill()
turtle.mainloop()
