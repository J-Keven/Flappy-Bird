import Bird
import pygame
from pygame.locals import *
import Diretories as D
import Floor
import Pipes
import random as rd
import time

pygame.init()
SCREENHEIGTH = 600
SCREENWIDTH = 400
POS_OBSTACLE = SCREENWIDTH
SLEEP_OBSTACLE = 1

SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGTH))
pygame.display.set_caption("Flapy Bird")
BACKGROUND = pygame.transform.scale(pygame.image.load(D.BACKGOUND), (SCREENWIDTH, SCREENHEIGTH))

flap = Bird.Bird(SCREENWIDTH, SCREENHEIGTH)
groupFlapy = pygame.sprite.Group()
groupFlapy.add(flap)

base = Floor.floor(SCREENWIDTH, SCREENHEIGTH)
group_base = pygame.sprite.Group()
group_base.add(base)

pipes = (Pipes.Pipe(SCREENWIDTH, SCREENHEIGTH), 
Pipes.Pipe(SCREENWIDTH + 200, SCREENHEIGTH),  
Pipes.Pipe(SCREENWIDTH + 400, SCREENHEIGTH)) 

gameover = pygame.image.load(D.GAMEOVER)

frame = pygame.time.Clock()
last = 2
while True:
    flag = True
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_SPACE and flag:
                flag = False
                flap.jump()
    
    frame.tick(20)
    SCREEN.blit(BACKGROUND, (0,0))
    groupFlapy.update()
    group_base.update()
    groupFlapy.draw(SCREEN)

    for index,i in enumerate(pipes):
        i.update(SCREEN)
        print(i.get_x)
        if flap.get_x == i.get_x :
            y_pipes = i.get_y
            print(y_pipes)
            if flap.get_y <= y_pipes[0]:
                pygame.quit()
                pass

            elif flap.get_y >= y_pipes[1]:
                pygame.quit()
                pass
                
            pass

        if i.start <= -50:
            i.start = pipes[last].start + 200
            i.image_higth = rd.randint(150, 350)
            last = index

    group_base.draw(SCREEN)
    SCREEN.blit(base.image, (base.rect[0]+SCREENWIDTH,SCREENHEIGTH - 100))
    POS_OBSTACLE = (POS_OBSTACLE - SLEEP_OBSTACLE) % SCREENWIDTH
    if flap.get_y >= base.get_y:
        SCREEN.blit(gameover, (100, 250))
        pygame.display.update()
        time.sleep(10)
        pygame.quit()
    
    if None:
        pass

    elif None:
        pass

    pygame.display.update()