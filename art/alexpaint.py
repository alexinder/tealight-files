from tealight.art import (color, line, spot, circle, box, image, text, background)

def DrawPalette(x,y, colors, w, h):
  for c in colors:
    if c == "rainbow":
      color("blue")
      box(x,y, w/3, h)
      color("red")
      box(x+h/3, y, w/3, h)
      color("pink")
      box(x+2*h/3, y, w/3, h)
    else: 
      color(c)
      box(x, y, w, h)
    y = y + h

    
colors = ["black",
          "grey", 
          "red",
          "magenta",
          "pink",
          "blue",
          "indigo",
          "purple",
          "limegreen",
          "forestgreen",
          "orange",
          "gold",
          "yellow",
          "rainbow"]    

x = 10
y = 10
w = 50
h= 55
DrawPalette(x,y, colors , w, h)

def color_click(mx,my):
  if mx > x and mx < x+w and my > y and my < y+(h*len(colors)):
    
      RowNo = (my-y)/h
  
      #color(colors[RowNo])
      print RowNo
      
      return colors[RowNo]
