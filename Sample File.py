import turtle
import math
def polygon(anna_hari,length,n):
    angle = 360/n
    for i in range(n):
        anna_hari.forward(length)
        anna_hari.rt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def circle(t, r):
    arc(t, r, 360)

anna_hari=turtle.Turtle()
anna_hari.fd(200)
anna_hari.rt(90)
anna_hari.fd(100)
anna_hari.rt(90)
anna_hari.fd(200)
anna_hari.rt(90)
anna_hari.fd(100)
anna_hari.mainloop()
'''
polygon(anna_hari,100,6)
polygon(anna_hari,90,6)
polygon(anna_hari,80,6)
polygon(anna_hari,70,6)
polygon(anna_hari,60,6)
circle(anna_hari,100)
turtle.mainloop()
circle(anna_hari,100)
circle(anna_hari,90)
circle(anna_hari,80)
circle(anna_hari,70)
circle(anna_hari,60)
anna_hari.circle(50)
anna_hari.circle(50)
anna_hari.circle(50)
'''
