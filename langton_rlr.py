import pygame
import time
import random


class Langton(object):

    def __init__(self, screenX, screenY, lifeSize, screen):
        self.screenX = screenX
        self.screenY = screenY
        self.lifeSize = lifeSize
        self.screen = screen
        self.lastPosX = 0
        self.lastPosY = 0
        self.curX = 0
        self.curY = 0
        self.LEFT = False
        self.RIGHT = False
        self.UP = False
        self.DOWN = False

    def savePos(self, newXY):
        self.curX = newXY[0]
        self.curY = newXY[1]

    def getCurPos(self):
        return self.curX, self.curY

    def initMove(self, initX, initY):
        return self.moveUp(initX, initY)

    def moveUp(self, x, y):
        newValueX = x
        newValueY = y - self.lifeSize
        if(newValueY < 0):
            newValueY = 0

        self.LEFT = False
        self.RIGHT = False
        self.UP = True
        self.DOWN = False

        return newValueX, newValueY

    def moveDown(self, x, y):
        newValueX = x
        newValueY = y + self.lifeSize
        if(newValueY > self.screenY):
            newValueY = self.screenY

        self.LEFT = False
        self.RIGHT = False
        self.UP = False
        self.DOWN = True

        return newValueX, newValueY

    def moveLeft(self, x, y):
        newValueY = y
        newValueX = x - self.lifeSize
        if(newValueX < 0):
            newValueX = 0

        self.LEFT = True
        self.RIGHT = False
        self.UP = False
        self.DOWN = False

        return newValueX, newValueY

    def moveRight(self, x, y):
        newValueY = y
        newValueX = x + self.lifeSize
        if(newValueX > self.screenX):
            newValueX = self.screenX

        self.LEFT = False
        self.RIGHT = True
        self.UP = False
        self.DOWN = False

        return newValueX, newValueY

    def getLastPos(self, x, y):
        if(self.LEFT):
            return x + self.lifeSize, y

        if(self.RIGHT):
            return x - self.lifeSize, y

        if(self.UP):
            return x, y + self.lifeSize

        if(self.DOWN):
            return x, y - self.lifeSize

        return x, y

    def checkOrientation(self, x, y, lastX, lastY):
        retX = x
        retY = y
        if(x - lastX == self.lifeSize):
            retX, retY = self.movement(x, y, lambda: self.moveUp(
                x, y), lambda: self.moveDown(x, y))
            # right

        if(x - lastX == -self.lifeSize):
            # left
            retX, retY = self.movement(x, y, lambda: self.moveDown(
                x, y), lambda: self.moveUp(x, y))

        if(y - lastY == -self.lifeSize):
            # up
            retX, retY = self.movement(x, y, lambda: self.moveLeft(
                x, y), lambda: self.moveRight(x, y))

        if(y - lastY == self.lifeSize):
            # down
            retX, retY = self.movement(x, y, lambda: self.moveRight(
                x, y), lambda: self.moveLeft(x, y))

        return retX, retY

    def movement(self, x, y, funcLeft, funcRight):
        dummyAplha = 0
        retX = 0
        retY = 0
        r = 0
        b = 0
        g = 0

        if(x >= self.screenX):
            x = self.screenX - self.lifeSize
        if(x <= 0):
            x = 0 + self.lifeSize
        if(y >= self.screenY):
            y = self.screenY - self.lifeSize
        if(y <= 0):
            y = 0 + self.lifeSize

        r, g, b, dummyAplha = self.screen.get_at((x, y))

        if(r == 255 and g == 255 and b == 255):
            #moveRight(x, y, (0, 0, 0))
            retX, retY = funcRight()
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                x, y, self.lifeSize, self.lifeSize))

        if(r == 0 and g == 0 and b == 0):
            #moveLeft(x, y, (0, 128, 255))
            retX, retY = funcLeft()
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                x, y, self.lifeSize, self.lifeSize))

        ''' if(r == 0 and g == 0 and b == 0):
            #moveLeft(x, y, (0, 128, 255))
            retX, retY = funcLeft()
            pygame.draw.rect(self.screen, (0, 128, 255), pygame.Rect(
                x, y, self.lifeSize, self.lifeSize)) '''

        ''' if(r == 0 and g == 128 and b == 255):
            #moveRight(x, y, (255, 255, 255))
            retX, retY = funcRight()
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                x, y, self.lifeSize, self.lifeSize)) '''

        return retX, retY
