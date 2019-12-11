import pygame
from pygame.locals import *
import Diretories as D
import random as rd

class Pipe():
    def __init__(self, width, heigth):
        
        self.screenwhidth = width
        self.__passage = 90
        self.image_higth = rd.randint(150, 350)
        self.__obstacle = [
            pygame.image.load(D.OBSTACLE).convert_alpha(),
            pygame.image.load(D.OBSTACLE).convert_alpha()]

        self.__obstacle[1] = pygame.transform.scale(self.__obstacle[1],(52,400))
        self.__obstacle[1] = pygame.transform.flip(self.__obstacle[1],0,1)
        self.start = width
        self.__sleep = 4

    def update(self, SCREEN):
        SCREEN.blit(self.__obstacle[1],(self.start,self.image_higth - 400))
        SCREEN.blit(self.__obstacle[0],(self.start,self.image_higth +  self.__passage))
        self.start -= self.__sleep
        
    def get_obstacle(self, position):
        return self.__obstacle[position]

    def getPisitios(self):
        pass
    
    @property
    def get_y(self):
        return (self.image_higth, self.image_higth +  self.__passage)

    @property
    def get_x(self):
        return self.start
