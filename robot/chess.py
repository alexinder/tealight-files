from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

distance = 100
for n in range(0,distance):
  move()
  
if touch()=='wall':
  turn(1)