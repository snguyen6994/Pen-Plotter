#Stephanie Nguyen
#CS 3-4 Period 2

from madison_axi.axi import *
from random import randrange

    #Stuffs:
#x_axis = randrange(-250, 250)
#y_axis = randrange(-180, 180)

#move_to(x_axis, y_axis)
#move_to(0, 0)

length_ = randrange(1, 51)

initialize()

#for x in range(0, 200):
  #move_forward(x*int(2))
  #turn_left(20)

for _ in range(5):
    for length in range(0, length_):
        length_ = randrange(1, 51)
        pen_down()
        move_forward(length*2)
        turn_left(100)
        pen_up()
    x_axis = randrange(-250, 250)
    y_axis = randrange(-180, 180)
    move_to(x_axis, y_axis)
    

cleanup()

