### IMPORTING
import pygame
import random
import config

class Peacock(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.minhungerpeace, self.maxhungerpeace = config.peacocks['minHungerPeace'], config.peacocks['maxHungerPeace']
        self.hunger= config.peacocks['startingHunger']
        self.speed= config.peacocks['avgSpeed']
        self.age = 0
        self.fertilibity= False
        self.flag = "peacock"

        self.image = pygame.image.load("images/pea.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()


    def create(self):
        self.weight = random.uniform(config.peacocks['minWeight'], config.peacocks['maxWeight'])
        self.speed = (config.peacocks['avgSpeed']*(4.5/self.weight))
        self.x = random.randint(1,100)
        self.y = random.randint(1,100)
        self.rect.x = self.x
        self.rect.y = self.y

    def move(self, screen_rect):
        # <- movement
        option=[-1,1]
        move_vertical=random.choice(option)*self.speed
        self.rect.y += move_vertical
        move_horizontal=random.choice(option)*self.speed
        self.rect.x += move_horizontal
        self.hunger -= config.peacocks['moveCost']
        self.rect.clamp_ip(screen_rect)


    def eat(self):
        # <- eating sth
        self.hunger += config.peacocks['eatingPoints']

    def be_eaten(self,animals_collision_list):
        # <- eaten by tiger
        for i in animals_collision_list:
            if self == i:
                die()

    def starve(self):
        # <- dying if too hungry
        if self.hunger == config.peacocks['minHunger']:
            return True

    def fertile(self):
        if self.hunger > config.peacocks['fertilityLvl']:
            self.fertilibity = True
        else:
            self.fertilibity = False

    def breed(self):
        self.hunger -= config.peacocks['fertilityCost']
        newone = Peacock()
        newone.weight = self.weight*random.triangular(-1,1)
        newone.speed = self.speed*random.triangular(-1,1)
        newone.rect.x = self.rect.x
        newone.rect.y = self.rect.y
        return newone
