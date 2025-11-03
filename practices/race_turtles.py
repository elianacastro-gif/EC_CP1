#EC 1st turtle raceing 
import turtle
import random

#name your impports/where your line wil be
line = turtle.Turtle()

line.hideturtle()

line.teleport(200,500)

line.right(90)

line.width(10)
line.forward(1000)

#create the turtles code
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()

#make spesific code inputs
t1.color("purple")
t1.shape("turtle")
t1.teleport(-400,300)

t2.color("green")
t2.shape("turtle")
t2.teleport(-400,150)

t3.color("pink")
t3.shape("turtle")
t3.teleport(-400,0)

t4.color("yellow")
t4.shape("turtle")
t4.teleport(-400,-150)

t5.color("blue")
t5.shape("turtle")
t5.teleport(-400,-300)

#create loop of where the turtles where go
while True:
    speed = random.randint(2,5)
    t1.forward(speed)
    if t1.xcor() >= 200:
        print("purple wins ")
        break
    t2.forward(speed)
    if t2.xcor() >= 200:
        print("green wins ")
        break
    t3.forward(speed)
    if t3.xcor() >= 200:
        print("pink wins ")
        break
    t4.forward(speed)
    if t4.xcor() >= 200:
        print("yellow wins ")
        break
    t5.forward(speed)
    if t5.xcor() >= 200:
        print("blue wins ")
        break



turtle.done()

#determine the winner

