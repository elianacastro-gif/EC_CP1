#EC 1st Maze Generator

import turtle
import random
#make two lists
maze = turtle.Turtle()










grid_columns = (random.randint(0,1))
grid_columns=[
    [(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1))],
    [(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1))],
    [(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),random.randint(0,1)],
    [(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1))],
    [(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1))]],


grid_rows = (random.randint(0,1))
grid_rows =[
    [(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1))],
    [(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1))],
    [(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1))],
    [(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1))],
    [(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1)),(random.randint(0,1))]]



for length in grid_rows:
    for wall in length:
        if wall >= 0:
            maze.penup()
            maze.forward(50)
        if wall <= 1:
            maze.pendown()
            maze.forward(50)
    maze.penup()
    maze.teleport(0,50)
  


maze_draw = turtle.Turtle()
maze_draw.hideturtle()
maze_draw.forward(50)
maze_draw.penup()
maze_draw.pendown()










turtle.done()