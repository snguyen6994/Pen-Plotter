#Stephanie Nguyen
#CS 3-4 Period 2

from madison_axi.axi import *
from random import randrange

    #Stuffs:
#x_axis = randrange(-500, 500)
#y_axis = randrange(-370, 370)

#move_to(x_axis, y_axis)
#move_to(0, 0)

length_ = randrange(1, 51)


def polygon(s, l):
  pen_up()
  num_sides = s

  pen_down()
  for angle in range(0, num_sides):
      move_forward(l)
      turn_left(360//int(num_sides))
  pen_up()

def flower():
    petals = randrange(4, 9)
    length__ = randrange(10, 20)
    shape = randrange(3, 9)
    for _ in range(petals):
        polygon(shape, length__)
        turn_left(360//int(petals))
  
def row_of_shapes(num_s, size, row, column):
  x = -450
  y = 320
  move_to(x, y)
  for _ in range(column):
      for _ in range(row):
          flower()
          point_in_direction(0)
          move_forward(90)
      y -= 90
      move_to(x, y)

initialize()
row_of_shapes(4, 25, 11, 8)
cleanup()

