#EC 1st tirtle raceing 
import turtle
import random


line = turtle.Turtle()

line.hideturtle()

line.teleport(200,500)

line.right(90)

line.width(10)
line.forward(1000)


t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()

t1.color("purple")
t1.shape("turtle")
t1.teleport(-400,300)
t1.forward()

t2.color("green")
t2.shape("turtle")
t2.teleport(-400,150)
t2.forward()

t3.color("pink")
t3.shape("turtle")
t3.teleport(-400,0)
t3.forward()

t4.color("yellow")
t4.shape("turtle")
t4.teleport(-400,-150)
t4.forward()

t5.color("blue")
t5.shape("turtle")
t5.teleport(-400,-300)
t5.forward()


turtle.done()