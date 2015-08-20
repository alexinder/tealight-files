from tealight.art import (color, line, spot, circle, box, image, text, background)

lastx = 0
lasty = 0

color("purple")

def handle_mousedown(x,y):
  global lastx, lasty
  
  lastx = x
  lasty = y

def handle_mousemove(x,y,button):
  global lastx, lasty
  
  if button == "left":
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y

color("black")
box(10, 75, 25, 25)

color("grey")
box(35, 75, 25, 25)

color("red")
box(10, 100, 25, 25)

color("blue")
box(35, 100, 25, 25)

color("green")
box(10, 125, 25, 25)

color("yellow")
box(35, 125, 25, 25)

color("orange")
box(10,150, 25, 25)

color("purple")
box(35, 150, 25, 25)

color("pink")
box(10, 175, 25, 25)

color("indigo")
box(35, 175, 25, 25)

color("violet")
box(10, 200, 25, 25)

color("aqua")
box(35, 200, 25, 25)

color("gold")
box(10, 225, 25, 25)

color("silver")
box(35, 225, 25, 25)

color("magenta")
box(10, 250, 25, 25)

color("chocolate")
box(35, 250, 25, 25)