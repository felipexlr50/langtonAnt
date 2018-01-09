import pygame
import time
import random

screenX = 800
screenY = 600

lifeSize = 5

lifeTime = 1

initX = random.randint(0, screenX)
initY = random.randint(0, screenY)

curX = initX
curY = initY

LEFT = False
RIGHT = False
UP = False
DOWN = False

moveList = []

runtime = 0

cont = 0


def saveMoves(move):
    moveList.append(move)


def isPrime(prime):
    count = 0
    if(prime < 2):
        return False

    if prime % 2 == 0:
        return False
    if prime % 3 == 0:
        return False

    for n in range(1, prime + 1):
        if(prime % n == 0):
            count += 1
        if(count > 2):
            return False
    return True


def moveUp(x, y):
    newValue = y - lifeSize
    if(newValue < 0):
        newValue = 0

    LEFT = False
    RIGHT = False
    UP = True
    DOWN = False

    saveMoves({'x': x, 'y': newValue})

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(
        x, newValue, lifeSize, lifeSize))

    return x, newValue


def moveDown(x, y):
    newValue = y + lifeSize
    if(newValue > screenY):
        newValue = screenY

    LEFT = False
    RIGHT = False
    UP = False
    DOWN = True

    saveMoves({'x': x, 'y': newValue})

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(
        x, newValue, lifeSize, lifeSize))

    return x, newValue


def moveLeft(x, y):
    newValue = x - lifeSize
    if(newValue < 0):
        newValue = 0

    LEFT = True
    RIGHT = False
    UP = False
    DOWN = False

    saveMoves({'x': newValue, 'y': y})

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(
        newValue, y, lifeSize, lifeSize))

    return moveDown(newValue, y)


def moveRight(x, y):
    newValue = x + lifeSize
    if(newValue > screenX):
        newValue = screenX

    LEFT = False
    RIGHT = True
    UP = False
    DOWN = False

    saveMoves({'x': newValue, 'y': y})

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(
        newValue, y, lifeSize, lifeSize))

    return newValue, y


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


def eraserMove(x, y):
    pygame.draw.rect(screen, (0, 0, 0),
                     pygame.Rect(x, y, lifeSize, lifeSize))


def eraseOldMoves():
    if(len(moveList) > lifeTime):
        pygame.draw.rect(screen, (0, 0, 0),
                         pygame.Rect(moveList[0]['x'], moveList[0]['y'], lifeSize, lifeSize))
        lastestMove = moveList.pop(0)


def mark(x, y, r, g, b):
    pygame.draw.rect(screen, (r, g, b),
                     pygame.Rect(x, y, lifeSize, lifeSize))


pygame.init()
screen = pygame.display.set_mode((screenX, screenY))
done = False

pygame.draw.rect(screen, (0, 128, 255),
                 pygame.Rect(initX, initY, lifeSize, lifeSize))

saveMoves({'x': initX, 'y': initY})

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            done = True

    cont += 1

    lastPosX, lastPosY = getLastPos(curX, curY)

    rand = random.randint(1, 1001)

    if(isPrime(rand)):
        mark(curX, curY, 255, 255, 0)
        curX, curY = moveUp(curX, curY)
        curX, curY = moveRight(curX, curY)

    elif(rand % 10 == 0):
        curX, curY = moveUp(curX, curY)
        #curX, curY = moveLeft(curX, curY)

    elif(rand % 7 == 0):
        curX, curY = moveUp(curX, curY)

    elif(rand % 5 == 0):
        curX, curY = moveDown(curX, curY)
        curX, curY = moveLeft(curX, curY)
        #eraserMove(lastPosX, lastPosY)

    elif(rand % 3 == 0):
        curX, curY = moveLeft(curX, curY)
        eraserMove(lastPosX, lastPosY)

    elif(rand % 2 == 0):
        curX, curY = moveRight(curX, curY)

    if(cont > 1000 and cont < 5000):
        curX, curY = moveUp(curX, curY)

    eraseOldMoves()
    pygame.display.update()
    time.sleep(runtime)
