from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

while n<10000:
  n=n+1
  print touch()
  if touch()=='fruit':
    move()