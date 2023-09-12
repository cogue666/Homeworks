from turtle import *

#let's build a house

#step 1: draw a square
speed (2)
width (5)
color("green")
begin_fill()
forward (200)
left (90)
forward (200)
left(90)
forward (200)
left (90)
forward (200) 
end_fill()

#step 2: Door

left(90)
forward(70)
color("black")
begin_fill()
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90)

end_fill()

penup()
goto (200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)

end_fill()

#WINDOW

penup()
goto(30, 130)
pendown()

begin_fill()
color("grey")
right(150)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
end_fill()


penup()
goto(120, 130)
pendown()

begin_fill()
color("grey")
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()







exitonclick()

