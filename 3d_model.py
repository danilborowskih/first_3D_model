import turtle
import math
s=100
l=90
n=-3
r=7
nw=0
turtle.speed(100000)
turtle.penup()
turtle.backward(s*3.5)
turtle.left(90)
turtle.forward(s)
turtle.right(90)
turtle.pendown()
turtle.hideturtle()
def cub(csize):
    for step in range(4):
        turtle.forward(csize)
        turtle.left(360/4)
def cub_line(n,r,nw):
    for step in range(r):
        k=(((s-l)/2-n*(s-l))**2+((s-l)/2+nw*(s-l))**2)**0.5
        c=(((s+l)/2+n*(s-l))**2+((s-l)/2+nw*(s-l))**2)**0.5
        cosa=(s**2+k**2-c**2)/(2*s*k)
        a=math.acos(cosa)*(180/math.pi)
        n+=1
        turtle.left(a)
        turtle.forward(k)
        turtle.right(a)
        cub(l)
        turtle.right(180-a)
        turtle.forward(k)
        turtle.left(180-a)
        cub(s)
        turtle.forward(s)
for i in range(3):
    cub_line(n,r,i)
    turtle.backward(r*s)
    turtle.right(90)
    turtle.forward(s)
    turtle.left(90)