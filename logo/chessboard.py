from tealight.logo import move, turn, color


def drawsquare():
  turn(90)
  move(25)
  turn(90)
  move(25)
  turn(90)
  move(25)
  turn(90)
  move(25)
  

def oneline():
  for i in range(0,4):
    turn(90)
    move(25)
  
oneline()