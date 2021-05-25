import pygame
import sys
import Square
import random

class Main:
    def __init__(self) -> None:
        self.running = True
        self.window = None
        self.tiles = []
        self.pTileImg = pygame.image.load("TilePressed.png")
        self.upTileImg = pygame.image.load("TileUnpressed.png")
        self.flagImg = pygame.image.load("Flag.png")
        self.mineNum = 50

    def drawWindow(self, width, height):
        w = width * self.upTileImg.get_width()
        h = height * self.upTileImg.get_height()
        self.window = pygame.display.set_mode((w,h))

    def populateTiles(self):
        th = 0
        while(th < self.window.get_height()):
            tx = 0
            while(tx < self.window.get_width()):
                tile = Square.square(self.window, tx, th, self.upTileImg, self.pTileImg, self.flagImg)
                self.tiles.append(tile)
                tx += self.upTileImg.get_width()
            th += self.upTileImg.get_height()

    def linkTiles(self):
        for tile in self.tiles:
            for subTile in self.tiles:
                if subTile.x >= (tile.x - tile.tileImg.get_width()) and subTile.x <= (tile.x + tile.tileImg.get_width()):
                    if subTile.y >= (tile.y - tile.tileImg.get_height()) and subTile.y<= (tile.y + tile.tileImg.get_height()):
                        tile.link(subTile)
                        if subTile.isMined:
                            tile.number += 1
    
    def mineUp(self, mineNum):
        while mineNum > 0:
            randTile = random.randint(0, len(self.tiles)-1)
            if not self.tiles[randTile].isMined:
                self.tiles[randTile].isMined = True
                mineNum -= 1

    def drawTiles(self):
        for t in self.tiles:
            t.draw()

    def start(self):
        pygame.init()
        self.drawWindow(20,20)
        self.populateTiles()
        self.mineUp(self.mineNum)
        self.linkTiles()
        #self.debug()
        while(self.running):
            self.update() 
    
    def update(self):
        self.drawTiles()
        mouse_state = pygame.mouse.get_pressed()
        pressedCount = 0
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
            if e.type == pygame.MOUSEBUTTONUP:
                mousePOS = pygame.mouse.get_pos()
                mouse_x = int(mousePOS[0]/self.upTileImg.get_width())*self.upTileImg.get_width()
                mouse_y = int(mousePOS[1]/self.upTileImg.get_height())*self.upTileImg.get_height()
                for tile in self.tiles:
                    if tile.x == mouse_x and tile.y == mouse_y:
                        if mouse_state == (1,0,0):
                            tile.press()
                        elif mouse_state== (0,0,1):
                            tile.flag()
                        elif mouse_state == (1,0,1):
                            if tile.number != 0:
                                tile.massPress()
                    if tile.isPressed:
                        if tile.isMined:
                            print("BOOM, you loose")
                            self.running = False
                        pressedCount += 1        
        if pressedCount == (len(self.tiles) - self.mineNum):
            print("you Win!")
            self.running = False
            pass

        pygame.display.flip()

    def debug(self):
        for t in self.tiles:
            t.showNeighbours()

if __name__ == "__main__":
    main = Main()
    main.start()
    pygame.quit()
    sys.exit()