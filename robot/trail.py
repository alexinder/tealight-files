from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

while n<10000:
  n++
  print touch()
  if touch()=='fruit':
    move()