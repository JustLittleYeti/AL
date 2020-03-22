### IMPORTING
import pygame
import random

def randomfloat():
    x=random.triangular(-1, 1, 0)
    return x

class Peacock(pygame.sprite.Sprite):

    def __init__(self):
        
        super().__init__()
        self.minweight, self.maxweight = 3, 6
        self.minhungerpeace, self.maxhungerpeace = 1, 5
        self.minhunger, self.maxhunger = 0, 100
        self.hunger= 50
        self.speed= 16
        self.age = 0

        self.image = pygame.image.load("images/pea.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def create(self):
        self.weight = random.uniform(self.minweight, self.maxweight)
        self.speed = (16*(4.5/self.weight))
        self.x = random.randint(1,100)
        self.y = random.randint(1,100)
        self.rect.x = self.x
        self.rect.y = self.y

    def move(self):
        # <- movement
        option=[-1,1]
        move_vertical=random.choice(option)*self.speed
        self.rect.y += move_vertical
        move_horizontal=random.choice(option)*self.speed
        self.rect.x += move_horizontal
        self.hunger -= 1

    def eat(self,food_collision_list):
        # <- eating sth
        for i in food_collision_list:
            if self == i:
                self.hunger+=20

    def be_eaten(self,animals_collision_list):
        # <- eaten by tiger
        for i in animals_collision_list:
            if self == i:
                die()

    def starve(self):
        # <- dying if too hungry
        if self.hunger == 0:
            die()

    def die(self):
        # <- for deleting object
        del self
