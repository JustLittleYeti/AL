import pygame
import random
import config

class Tiger(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/tig.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.tigersList  = pygame.sprite.Group()


    def create(self, window):
        self.weight = random.uniform(config.tigers['minWeight'], config.tigers['maxWeight'])
        self.speed = (config.tigers['avgSpeed']*(182.5/self.weight))
        self.x = random.randint(600,700)
        self.y = random.randint(400,500)
        self.rect.x = self.x
        self.rect.y = self.y
        self.hunger = config.tigers['startingHunger']
        self.tigersList.update()
        self.tigersList.draw(window)

    def move(self, window, window_rect):
        option=[-1,1]
        for tiger in self.tigersList:
            move_horizontal=random.choice(option)*tiger.speed
            tiger.rect.x += move_horizontal
            move_vertical=random.choice(option)*tiger.speed
            tiger.rect.y += move_vertical
            tiger.hunger -= config.tigers['moveCost']
            tiger.rect.clamp_ip(window_rect)
        self.tigersList.update()
        self.tigersList.draw(window)

    def eat(self, AnimalCollisionsList):
        for tiger in AnimalCollisionsList:
            tiger.hunger += config.tigers['eatingPoints']
            self.tigersList.update()

    def starve(self):
        for tiger in self.tigersList:
            if tiger.hunger == 0:
                self.tigersList.remove(tiger)
                self.tigersList.update()

    def breed(self, window):
        for tiger in self.tigersList:
            if tiger.hunger >= config.tigers['fertilityLvl']:

                newone = Tiger()
                newone.create(window)
                self.tigersList.add(newone)
                self.tigersList.update()
                #self.all_animals_list.update()
                self.tigersList.draw(window)

    '''def collide(self, tigersList, AnimalCollisionsList):
        for tiger in collisionsList.keys():'''

    def manageEventsTigers(self, AnimalCollisionsList, window, window_rect):
        print("Tigers: ", len(self.tigersList))
        self.eat(AnimalCollisionsList)
        self.move(window, window_rect)
        self.eat(AnimalCollisionsList)
        self.starve()
        self.breed(window)
