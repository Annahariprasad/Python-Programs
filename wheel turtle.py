import turtle

def wheel():
    for i in range(8):
        t.rt(90)
        t.fd(100)
        t.lt(90)
        t.circle(100,45)
        t.lt(90)
        t.fd(100)
        t.rt(90)

t = turtle.Turtle()
t.pensize(2)
wheel()
print('NAME : ANNA HARIPRASAD')
print('REGD NO : 19X51A0503')
turtle.mainloop()


