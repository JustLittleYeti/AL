### IMPORTING
import pygame
import random

def randomfloat():
    x=random.triangular(-1, 1, 0)
    return x

class Food(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("images/apple.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.freshness = 10

    def create(self,food):
        for k in range(5):
            k=Food()
            food.add(k)
            k.place()

    def place(self):
        self.x = random.randint(0,700)
        self.y = random.randint(0,500)
        self.rect.x = self.x
        self.rect.y = self.y

    def be_eaten(self,food_collision_list):
        for i in food_collision_list:
            if self == i:
                del self

    def rotting(self):
        self.freshness -= 1

    def dissapear(self):
        if self.freshness <= 0:
            del self
            #not w
