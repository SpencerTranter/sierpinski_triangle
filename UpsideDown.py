import turtle # This imports the turtle library

'''
This method draws a triangle and fills it with the appropriate color
Parameters: x, y coordiantes, color specified, myTurtle variable
creating the turtle
'''
def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color) # fills the area drawn with a color
    myTurtle.up() # moves the turtle to face upwards
    '''
    Directs the turtle to move from coordinates of point 0.x, point
    0.y to point 0.x, 1.y
    '''
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down() # moves the turtle to face downwards
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

'''
Method to find the middle of the triangle
Parameters: takes two points
'''
def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['Blue','Medium Aquamarine','Medium Spring Green','Light Sky Blue','green',
                'red','blue'] # colors to be used set in an array
    '''
    Calls drawTriangle() method passing it the parameters points,
    colormap with degree (set as 3) as its number meaning as the
    variable degree goes down it will then choose the next color
    to the left in the array, and fianlly myTurtle to allow the
    turtle to perform its commands
    '''
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0: # loop continures as long as degree is greater than 0
        sierpinski([points[0], #draws the first of three triangles
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   '''
   Coordinates set in an array, used to find triangles size
   '''
   myPoints = [[200,100],[0,-200],[-200,100]]
   '''
   Calls sierpinski method which in turn will call itself to create the
   three layers of triangles
   Parameters: myPoints the variable listed above, 3 for the variable degree,
   and myTurtle
   '''
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

main()
