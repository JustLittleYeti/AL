### IMPORTING
import pygame
import random
import config

class Food(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("images/apple.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
######################################################3
        self.freshness = config.food['freshness']
        self.flag = "food"


    def create(self):
        #####################################################3
        self.x = random.randint(0,700)
        self.y = random.randint(0,500)
        self.rect.x = self.x
        self.rect.y = self.y

    def be_eaten(self,food_collision_list):
        for i in food_collision_list:
            if i.flag == "food":
                return True

    def rotting(self):
        self.freshness -= config.food['rottingPeace']
        if self.freshness == 0:
            return True
