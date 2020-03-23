import pygame
import random
import config

class Tiger(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.minhungerpeace, self.maxhungerpeace = config.tigers['minHungerPeace'], config.tigers['maxHungerPeace']
        self.hunger= config.tigers['startingHunger']
        self.speed= config.tigers['avgSpeed']
        self.age = 0
        self.flag = "tiger"

        self.image = pygame.image.load("images/tig.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def create(self):
        self.weight = random.uniform(config.tigers['minWeight'], config.tigers['maxWeight'])
        self.speed = (config.tigers['avgSpeed']*(182.5/self.weight))
        self.x = random.randint(600,700)
        self.y = random.randint(400,500)
        self.rect.x = self.x
        self.rect.y = self.y

    def move(self, screen_rect):
        option=[-1,1]
        move_vertical=random.choice(option)*self.speed
        self.rect.y += move_vertical
        move_horizontal=random.choice(option)*self.speed
        self.rect.x += move_horizontal
        self.hunger -= config.tigers['moveCost']
        self.rect.clamp_ip(screen_rect)

    '''def eat(self):
        # <- eating sth
            self.hunger+= config.tigers['eatingPoints']'''

    def starve(self):
        # <- dying if too hungry
        if self.hunger == config.tigers['minHunger']:
            return True
