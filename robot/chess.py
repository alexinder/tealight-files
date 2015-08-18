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
    
def turnrightand4():
  turn(1) 
  distance = 4
  for n in range(0,distance):
    move()
    
def turnleftand4():
  turn(-1) 
  distance = 4
  for n in range(0,distance):
    move()

move32()
turnrightand4()
turn(1)
move32()
turnleftand4()
turn(-1)
move32()
turnrightand4()
turn(1)
move32()
turnleftand4()

