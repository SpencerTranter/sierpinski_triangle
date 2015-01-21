import turtle
'''
Tree method, creates the recursive desighn for the tree
Paramaters: branchLen used to determin the trees size and amoung of recursion,
as well as t which passes in turtle
'''
def tree(branchLen,t):
    if branchLen > 5: #branchLen has a minimum of 5
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    treeSize = 100 #size I set branchLen to be
    rotate90 = 90 #if I need to rotate 90 one way or another
    treeSpace = 100 #space between each tree
    numTrees = 3 #number of trees between far left and the right on the right
    t = turtle.Turtle() #imports turtle to the program
    myWin = turtle.Screen()
    myWin.bgcolor("black") #changes the background color to black

    t.left(rotate90)#first tree
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(treeSize,t)

    t.left(rotate90)
    t.up()
    t.forward(treeSpace)
    t.right(rotate90)
    t.down()
    t.color("red")
    tree(treeSize,t)

    t.left(rotate90)
    t.up()
    t.forward(treeSpace)
    t.right(rotate90)
    t.down()
    t.color("blue")
    tree(treeSize,t)

    t.right(rotate90)
    t.up()
    t.forward(treeSpace * numTrees)
    t.left(rotate90)
    t.down()
    t.color("red")
    tree(treeSize,t)

    t.right(rotate90)
    t.up()
    t.forward(treeSpace)
    t.left(rotate90)
    t.down()
    t.color("blue")
    tree(treeSize,t)
    myWin.exitonclick()

main()


'''
Citations:
http://interactivepython.org/runestone/static/pythonds/Recursion/graphical.html
https://docs.python.org/2/library/turtle.html
'''
