from tealight.art import (color, line, spot, circle, box, image, text, background)

def DrawPalette(x,y, colors, w, h):
  for c in colors:
    if c == "rainbow":
      box(
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

x = 100
y = 75
w = 25
h= 25
DrawPalette(x,y, colors , w, h)

def color_click(mx,my):
  if mx > x and mx < x+w and my > y and my < y+(h*len(colors)):
    
      RowNo = (my-y)/h
  
      #color(colors[RowNo])
      print RowNo
      
      return colors[RowNo]
