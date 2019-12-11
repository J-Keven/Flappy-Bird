import pygame
from pygame.locals import *
import Diretories as D

class Bird(pygame.sprite.Sprite):
    def __init__(self, SCREENWIDTH, SCREENHEIGTH):
        pygame.sprite.Sprite.__init__(self)
        self.__Max_Higth = 0
        self.__SPEED = 10
        self.current_imagen = 0
        self.x = SCREENHEIGTH / 2
        self.y = SCREENWIDTH / 2
        self.__Imagens = self.LoadImagens()
        self.image = pygame.image.load(D.BIRDMID).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = self.y
        self.rect[1] = self.x
        self.__caindo = True
        print(self.rect)

    def LoadImagens(self):
        imagens = [
            pygame.transform.scale(pygame.image.load( D.BIRDUP).convert_alpha(),(35,24)),
            pygame.transform.scale(pygame.image.load(D.BIRDMID).convert_alpha(),(35,24)),
            pygame.transform.scale(pygame.image.load( D.BIRDDOWN).convert_alpha(),(35,24))]
        return imagens
    
    def jump(self):
        self.__Max_Higth = 100
        self.__caindo = False
        self.__SPEED = 10

    def update(self):
        self.current_imagen = (self.current_imagen + 1) % 3 
        self.image = self.__Imagens[self.current_imagen]
        if self.rect[1] > -20 and not self.__caindo and self.__Max_Higth > 0:
            self.__Max_Higth -= self.__SPEED
            self.rect[1] -= self.__SPEED
            self.__SPEED -= 1

        else:
            self.__caindo = True
            self.rect[1] += 10
    
    @property
    def get_x(self):
        return self.rect[0]

    @property
    def get_y(self):
        return self.rect[1]

    @property
    def get_heigth(self):
        return self.rect[-1]

    @property
    def get_width(self):
        return self.rect[2]

    