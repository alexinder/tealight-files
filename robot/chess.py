from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
def move32():
 distance = 32
 for n in range(0,distance):
    move()
    
def turnand4():
  turn(1) 
  distance = 4
 for n in range(0,distance):
    move()

move32()
turnand4()

