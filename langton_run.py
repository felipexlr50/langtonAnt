import pygame
import time
import random
import langton_rlr as lan


screenX = int(input('Set screen X size(Default 800): '))
screenY = int(input('Set screen Y size(Default 600): '))

lifeSize = int(input('Set life pixel size(Default 5): '))

fps = int(input('Set runtime delay in sec(Default 60): '))


pygame.init()
screen = pygame.display.set_mode((screenX, screenY))
done = False
clock = pygame.time.Clock()


antList = []
while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            print(event.button)
            if(event.button == 1):
                ant = lan.Langton(screenX, screenY, lifeSize, screen)
                # init movement
                mouX, mouY = pygame.mouse.get_pos()
                ant.savePos(ant.initMove(mouX, mouY))
                antList.append(ant)
            elif(event.button == 3):
                antList.pop()

    for ant in antList:
        curXY = ant.getCurPos()
        lastPosXY = ant.getLastPos(curXY[0], curXY[1])

        ant.savePos(ant.checkOrientation(
            curXY[0], curXY[1], lastPosXY[0], lastPosXY[1]))

    pygame.display.update()
    # time.sleep(runtime)
    clock.tick(60)
