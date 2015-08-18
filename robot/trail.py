from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
n=0
while n<1000:
  n=n+1
  print touch()
  if touch()=='fruit':
    move()
  elif touch()==None:
    if right_side()=='fruit':
      turn(1)
    elif left_side()=='fruit':
      turn(-1)

