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
        if wall >= (0,1):
            maze.penup(50)
        if wall <= (0,1):
            maze.pendown(50)




maze_draw = turtle.Turtle()
maze_draw.hideturtle()
maze_draw.forward(50)
maze_draw.penup()
maze_draw.pendown()










turtle.done()