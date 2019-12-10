import pygame
from pygame.locals import *
import Diretories as D

class floor(pygame.sprite.Sprite):
    def __init__(self,SCREENWIDTH, SCREENHEIGTH):
        pygame.sprite.Sprite.__init__(self)
        self.__SPEED_BASE = 1
        self.image = pygame.transform.scale(pygame.image.load(D.FLOOR).convert_alpha(),(SCREENWIDTH, 100))
        self.rect = self.image.get_rect()
        self.rect[1] = SCREENHEIGTH - 100

    def update(self):
        self.rect[0] -= self.__SPEED_BASE
        if(self.rect[0] + self.rect[2] == 0):
            self.rect[0] = 0
  
    @property
    def get_x(self):
        return self.rect[0]

    @property
    def get_y(self):
        return self.rect[1]