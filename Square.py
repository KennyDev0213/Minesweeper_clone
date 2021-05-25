from pygame import font

class square():
    def __init__(self, window, x, y, tileImg, pressedTileImg,  flagImg) -> None:
        
        self.window = window
        self.tileImg = tileImg
        self.pressedTileImg = pressedTileImg
        self.flagImg = flagImg
        self.image = tileImg
        self.x = x
        self.y = y
        self.font = font.SysFont("arial", self.image.get_width())
        
        self.neighbours = []
        self.number = 0

        self.isMined = False
        self.isFlagged = False
        self.isPressed = False
        
    
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
        if self.isPressed:
            self.showNumber()
        elif self.isFlagged:
            self.window.blit(self.flagImg, (self.x, self.y))
        
    def press(self):
        if not self.isPressed and not self.isFlagged:
            self.isPressed = True
            self.image = self.pressedTileImg
            if self.number == 0:
                for tile in self.neighbours:
                    tile.press()
    
    def massPress(self):
        flagNum = 0
        for n in self.neighbours:
            if n.isFlagged:
                flagNum += 1
        if flagNum == self.number:
            for n2 in self.neighbours:
                n2.press()

    def flag(self):
        if not self.isFlagged:
            self.isFlagged = True
        else:
            self.isFlagged = False
    
    def link(self, mine):
        self.neighbours.append(mine)

    def showNumber(self):
        wh = int(self.tileImg.get_width()/2)
        num = None
        if not self.isMined:
            if self.number == 0:
                pass
            elif self.number == 1:
                num = self.font.render(str(self.number),self.window,(18,125,255))
            elif self.number == 2:
                num = self.font.render(str(self.number),self.window,(18,255,93))
            elif self.number == 3:
                num = self.font.render(str(self.number),self.window,(255,18,18))
            elif self.number == 4:
                num = self.font.render(str(self.number),self.window,(255,18,172))
            elif self.number == 5:
                num = self.font.render(str(self.number),self.window,(16,13,105))
            elif self.number == 6:
                num = self.font.render(str(self.number),self.window,(87,65,19))
            elif self.number == 7:
                num = self.font.render(str(self.number),self.window,(14,41,13))
            elif self.number == 8:
                num = self.font.render(str(self.number),self.window,(55,19,87))
        
        if num != None:
            numX = wh - (num.get_width()/2) + self.x
            numY = wh - (num.get_height()/2) + self.y

            self.window.blit(num, (numX, numY))
    
    def showNeighbours(self):
        me = "["+str(self.x)+", "+str(self.y)+"] => "
        myNeighbours = ""
        for n in self.neighbours:
            myNeighbours += "["+str(n.x)+", "+str(n.y)+"] "
        print(me + myNeighbours)