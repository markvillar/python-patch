def drawPatchWindow():
    win = GraphWin("Patch Design Number 9", 100, 100)
    radius = 10
    yCord = 90
    for i in range(10):
        circle = Circle(Point(50, yCord), radius)
        circle.draw(win)
        circle.setOutline("red")
        radius = radius + 10
        yCord = yCord - 10

def PenultimateLargeWindow():
    scale = 5
    win = GraphWin("Penultimate Design", 100*scale, 100*scale)
    
    #Five Red Patches (Rows)
    topLeftYCord = 0
    bottomRightYCord = 10 * scale
    
    for i in range(5):
        #Six Red Patches (Columns)
        topLeftXCord = -5 * scale
        bottomRightXCord = 5 * scale
        
        for j in range(6):
            redShade = Rectangle(Point(topLeftXCord, topLeftYCord), Point(bottomRightXCord, bottomRightYCord))
            redShade.setFill("red")
            redShade.draw(win)
            
            topLeftXCord = topLeftXCord + (20 * scale)
            bottomRightXCord = bottomRightXCord + (20 * scale)
        
        topLeftYCord = topLeftYCord + (20 * scale)
        bottomRightYCord = bottomRightYCord + (20 * scale)

    #White Spaces
    whiteRectTopLeftYCord = 10 * scale
    whiteBottomRightYCord = 20 * scale
    
    for l in range(5):
        #Rows
        whiteRectTopLeftXCord = 0
        whiteBottomRightXCord = 20 * scale
        
        for k in range(5):
            rect = Rectangle(Point(whiteRectTopLeftXCord, whiteRectTopLeftYCord), Point(whiteBottomRightXCord, whiteBottomRightYCord))
            rect.draw(win)
            whiteRectTopLeftXCord = whiteRectTopLeftXCord + (20 * scale)
            whiteBottomRightXCord = whiteBottomRightXCord + (20 * scale)

        whiteRectTopLeftYCord = whiteRectTopLeftYCord + (20 * scale)
        whiteBottomRightYCord = whiteBottomRightYCord + (20 * scale)

def PenultimateSmallWindow():
    win = GraphWin("Penultimate Design", 100, 100)
    
    #Five Red Patches (Rows)
    topLeftYCord = 0
    bottomRightYCord = 10
    
    for i in range(5):
        #Six Red Patches (Columns)
        topLeftXCord = -5
        bottomRightXCord = 5
        
        for j in range(6):
            redShade = Rectangle(Point(topLeftXCord, topLeftYCord), Point(bottomRightXCord, bottomRightYCord))
            redShade.setFill("red")
            redShade.draw(win)
            
            topLeftXCord = topLeftXCord + (20)
            bottomRightXCord = bottomRightXCord + (20)
        
        topLeftYCord = topLeftYCord + (20)
        bottomRightYCord = bottomRightYCord + (20)

    #White Spaces
    whiteRectTopLeftYCord = 10
    whiteBottomRightYCord = 20
    
    for l in range(5):
        #Rows
        whiteRectTopLeftXCord = 0
        whiteBottomRightXCord = 20
        
        for k in range(5):
            rect = Rectangle(Point(whiteRectTopLeftXCord, whiteRectTopLeftYCord), Point(whiteBottomRightXCord, whiteBottomRightYCord))
            rect.draw(win)
            whiteRectTopLeftXCord = whiteRectTopLeftXCord + (20)
            whiteBottomRightXCord = whiteBottomRightXCord + (20)

        whiteRectTopLeftYCord = whiteRectTopLeftYCord + (20)
        whiteBottomRightYCord = whiteBottomRightYCord + (20)