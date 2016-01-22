import turtle

# This funtion is making the top rhombus of a cube 
def drawTopRhombus(myTurtle):
  count = 0
  while count < 1:
    myTurtle.fillcolor("dark red")
    myTurtle.begin_fill()
    myTurtle.left(30)
    myTurtle.forward(20)
    myTurtle.left(120)
    myTurtle.forward(20)
    myTurtle.left(60)
    myTurtle.forward(20)
    myTurtle.left(120)
    myTurtle.forward(20)
    myTurtle.left(30)
    myTurtle.end_fill()
    count = count + 1

# this is the rhombus of the right side of the cube  
def drawRightRhombus(myTurtle):
    count = 0
    while count < 1:
      myTurtle.fillcolor("red")
      myTurtle.begin_fill()
      myTurtle.left(90)
      myTurtle.forward(20)
      myTurtle.right(60)
      myTurtle.forward(20)
      myTurtle.right(120)
      myTurtle.forward(20)
      myTurtle.right(60)
      myTurtle.forward(20)
      myTurtle.end_fill()
      count = count + 1
# this is the left rhombus of the cube      
def drawLeftRhombus(myTurtle):
  count = 0 
  while count < 1:
    myTurtle.fillcolor("orange")
    myTurtle.begin_fill()
    myTurtle.right(60)
    myTurtle.forward(20)
    myTurtle.left(120)
    myTurtle.forward(20)
    myTurtle.left(60)
    myTurtle.forward(20)
    myTurtle.left(120)
    myTurtle.forward(20)
    myTurtle.end_fill()
    count = count + 1 
# Changing the turtle name to rocky
rocky = turtle.Turtle()
# Changing the speed of our turtle so it an go more quickly 
rocky.speed(0)

# this function puts all the rhombuses together in order to make a cube
def makeCube(rocky):
  count = 0
  while count < 1:
    drawTopRhombus(rocky) 
    rocky.penup()
    rocky.right(90)
    rocky.forward(20)
    rocky.left(90)
    rocky.pendown()
    drawRightRhombus(rocky)
    rocky.penup()
    rocky.right(120)
    rocky.forward(20)
    rocky.left(120)
    rocky.pendown()
    drawLeftRhombus(rocky)
    count = count + 1
    
# this sets up the position where the first row of cubes will be
makeCube(rocky)
rocky.penup()
rocky.right(60)
rocky.forward(20)
rocky.right(60)
rocky.forward(20)
rocky.left(30)
rocky.pendown()
makeCube(rocky)

# this creates and moves the squares in a horizontal line
def rowCube(rocky):
  count = 0
  while count < 5:
    rocky.penup()
    rocky.right(60)
    rocky.forward(20)
    rocky.right(60)
    rocky.forward(20)
    rocky.left(30)
    rocky.pendown()
    makeCube(rocky)
    count = count + 1

# This sets the position and creats a horizontal row of cubes on top
def topRow(rocky):
  count = 0
  while count < 1:
    rocky.penup()
    rocky.left(120)
    rocky.forward(220)
    rocky.right(120)
    rocky.forward(80)
    rowCube(rocky)
    count = count + 1
# top and middle row functions 
rowCube(rocky)
topRow(rocky)

# moves the pen where the bottom row of cubes will start at
rocky.penup()
rocky.left(100)
rocky.forward(200)
rocky.right(160)
rocky.forward(45)
rocky.right(30)
rocky.right(90)
rocky.forward(18)
rocky.left(90)
rocky.forward(2)
rocky.pendown()
makeCube(rocky)
rocky.right(60)
rocky.forward(20)
rocky.right(60)
rocky.forward(20)
rocky.left(30)

# this fuction makes the last row of cubes at the bottom 
def bottomRow(rocky):
  count = 0
  while count < 5:
    makeCube(rocky)
    rocky.right(60)
    rocky.forward(20)
    rocky.right(60)
    rocky.forward(20)
    rocky.left(30)
    count = count + 1

# bottom row function
bottomRow(rocky)

myTurtle.exitonclick()
