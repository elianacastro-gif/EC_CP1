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

speed = random.randint(2,5)
#create loop of where the turtles where go
for num in range(speed):
    t1.forward(speed)
    if t1.xcor() >= 200:
        print("purple wins ")
    t2.forward(speed)
    if t2.xcor() >= 200:
        print("green wins ")
    t3.forward(random.randint(2,5))
    if t3.xcor() >= 200:
        print("pink wins ")
    t4.forward(random.randint(2,5))
    if t4.xcor() >= 200:
        print("yellow wins ")
    t5.forward(random.randint(2,5))
    if t5.xcor() >= 200:
        print("blue wins ")
    



    turtle.done()

#determine the winner

