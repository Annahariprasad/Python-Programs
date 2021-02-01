#Arcimedean Spiral

import turtle

def draw_spiral(t,n,l,a,b):
    theta = 0
    for i in range(n):
        t.fd(l)
        dtheta = 1/(a+b*theta)
        t.lt(dtheta)
        theta+=dtheta

t = turtle.Turtle()
draw_spiral(t,1000,3,0.1,0.0002)
print('NAME : ANNA HARIPRASAD')
print('REGD NO : 19X51A0503')


