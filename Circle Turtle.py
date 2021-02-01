import turtle,math

def circle(t,l,a,n):
    for i in range(n):
        t.fd(l)
        t.lt(a)
        
t = turtle.Turtle()
t.color('red','blue')
t.pensize(2)
r = int(input('Enter radius : '))
n = int(input('Enter no. of parts : '))
cir = (2*math.pi*r)
l = cir/n
a = 360/n
t.begin_fill()
circle(t,l,a,n)
t.end_fill()
turtle.mainloop()
