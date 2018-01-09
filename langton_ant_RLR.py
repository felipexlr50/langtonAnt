import pygame
import time
import random


screenX = 800
screenY = 600

lifeSize = 5

runtime = 0

initX = random.randint(0, screenX)
initY = random.randint(0, screenY)

curX = initX
curY = initY

lastPosX = 0
lastPoxY = 0

r = 0
g = 0
b = 0

LEFT = False
RIGHT = False
UP = False
DOWN = False


def moveUp(x, y):
    newValueX = x
    newValueY = y - lifeSize
    if(newValueY < 0):
        newValueY = 0

    global LEFT
    global RIGHT
    global UP
    global DOWN

    LEFT = False
    RIGHT = False
    UP = True
    DOWN = False

    return newValueX, newValueY


def moveDown(x, y):
    newValueX = x
    newValueY = y + lifeSize
    if(newValueY > screenY):
        newValueY = screenY

    global LEFT
    global RIGHT
    global UP
    global DOWN

    LEFT = False
    RIGHT = False
    UP = False
    DOWN = True

    return newValueX, newValueY


def moveLeft(x, y):
    newValueY = y
    newValueX = x - lifeSize
    if(newValueX < 0):
        newValueX = 0

    global LEFT
    global RIGHT
    global UP
    global DOWN

    LEFT = True
    RIGHT = False
    UP = False
    DOWN = False

    return newValueX, newValueY


def moveRight(x, y):
    newValueY = y
    newValueX = x + lifeSize
    if(newValueX > screenX):
        newValueX = screenX

    global LEFT
    global RIGHT
    global UP
    global DOWN

    LEFT = False
    RIGHT = True
    UP = False
    DOWN = False

    return newValueX, newValueY


def getLastPos(x, y):
    if(LEFT):
        return x + lifeSize, y

    if(RIGHT):
        return x - lifeSize, y

    if(UP):
        return x, y + lifeSize

    if(DOWN):
        return x, y - lifeSize

    return x, y


def checkOrientation(x, y, lastX, lastY, screen):
    retX = x
    retY = y
    if(x - lastX == lifeSize):
        retX, retY = movement(x, y, screen, lambda: moveUp(
            x, y), lambda: moveDown(x, y))
        # right

    if(x - lastX == -lifeSize):
        # left
        retX, retY = movement(x, y, screen, lambda: moveDown(
            x, y), lambda: moveUp(x, y))

    if(y - lastY == -lifeSize):
        # up
        retX, retY = movement(x, y, screen, lambda: moveLeft(
            x, y), lambda: moveRight(x, y))

    if(y - lastY == lifeSize):
        # down
        retX, retY = movement(x, y, screen, lambda: moveRight(
            x, y), lambda: moveLeft(x, y))

    return retX, retY


def movement(x, y, screen, funcLeft, funcRight):
    dummyAplha = 0
    retX = 0
    retY = 0
    r = 0
    b = 0
    g = 0

    if(x >= screenX):
        x = screenX - lifeSize
    if(x <= 0):
        x = 0 + lifeSize
    if(y >= screenY):
        y = screenY - lifeSize
    if(y <= 0):
        y = 0 + lifeSize

    r, g, b, dummyAplha = screen.get_at((x, y))

    if(r == 255 and g == 255 and b == 255):
        #moveRight(x, y, (0, 0, 0))
        retX, retY = funcRight()
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(
            x, y, lifeSize, lifeSize))

    if(r == 0 and g == 0 and b == 0):
        #moveLeft(x, y, (0, 128, 255))
        retX, retY = funcLeft()
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(
            x, y, lifeSize, lifeSize))

    if(r == 0 and g == 128 and b == 255):
        #moveRight(x, y, (255, 255, 255))
        retX, retY = funcRight()
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
            x, y, lifeSize, lifeSize))

    return retX, retY


################################################################
pygame.init()
screen = pygame.display.set_mode((screenX, screenY))
done = False

# init movement
curX, curY = moveUp(initX, initY)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            done = True

    lastPosX, lastPoxY = getLastPos(curX, curY)

    curX, curY = checkOrientation(curX, curY, lastPosX, lastPoxY, screen)
    pygame.display.update()
    time.sleep(runtime)
