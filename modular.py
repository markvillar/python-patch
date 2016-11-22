from graphics import *

def shade(window, topLeftX, topLeftY, bottomRightX, bottomRightY, colour):
    rect = Rectangle(Point(topLeftX, topLeftY), Point(bottomRightX, bottomRightY))
    rect.setFill(colour)
    rect.draw(window)

def penultimatePatch():    
    win = GraphWin("Window", 100, 100)

    #Half Red Squares (Edges)
    topLeftX = 0
    topLeftY = 0
    
    bottomRightX = 5
    bottomRightY = 10
    
    for j in range(4):
        shade(win, topLeftX, topLeftY, bottomRightX, bottomRightY, "red")
        #Move all the way to the right
        topLeftX = topLeftX + 95
        bottomRightX = bottomRightX + 95

    #Midde Red Squares
    topLeftX = 15
    topLeftY = 0
    
    bottomRightX = 25
    bottomRightY = 10
    
    for i in range(4):
        shade(win, topLeftX, topLeftY, bottomRightX, bottomRightY, "red")
        #Move both X coordinates to the right
        topLeftX = topLeftX + 20
        bottomRightX = bottomRightX + 20

    #White Rows
    topLeftX = 0
    topLeftY = 10
    
    bottomRightX = 20
    bottomRightY = 20
    
    for k in range(5):
        shade(win, topLeftX, topLeftY, bottomRightX, bottomRightY, "white")
        #Move coordinates to the right
        topLeftX = topLeftX + 20
        bottomRightX = bottomRightX + 20