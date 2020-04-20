import pygame
import random
import config

class Animal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animalsList  = pygame.sprite.Group()
        self.peacocksList  = pygame.sprite.Group()
        self.tigersList  = pygame.sprite.Group()

    def moveHor(fauna, zwrot):
        move_horizontal=zwrot*fauna.speed
        fauna.rect.x += move_horizontal

    def moveVer(fauna, zwrot):
        move_vertical=zwrot*fauna.speed
        fauna.rect.y += move_vertical

    def move(self, window, window_rect, foodList):
        # <- movement
        option=[-1,1]
        for fauna in self.animalsList:
            if fauna.hunger >= 50:
                fauna.moveHor(random.choice(option))
                fauna.moveVer(random.choice(option))
                fauna.rect.clamp_ip(window_rect)
            elif fauna.hunger <= 50:
                pos = pygame.math.Vector2(fauna.x, fauna.y)
                if fauna.type == "peacock":
                    foodList = foodList
                elif fauna.type == "tiger":
                    foodList = self.peacocksList

                food = min([food for food in foodList], key=lambda food: pos.distance_to(pygame.math.Vector2(food.x, food.y)))
                if food.x > fauna.speed:
                    zwrotX = (food.x - fauna.x)
                    if zwrotX>0:
                        fauna.moveHor(1)
                    if zwrotX<0:
                        fauna.moveHor(-1)
                else:
                    # x < peacock.speed:
                    fauna.rect.x = food.x
                if food.y > fauna.speed:
                    zwrotY = (food.y - fauna.y)
                    if zwrotY>0:
                        fauna.moveVer(1)
                    if zwrotY<0:
                        fauna.moveVer(-1)
                else:
                    # y < peacock.speed:
                    fauna.rect.y = food.y
                #peacock.moveVer(zwrotY)
            if fauna.type == "peacock":
                fauna.hunger -= config.peacocks['moveCost']
            elif fauna.type == "tiger":
                fauna.hunger -= config.tigers['moveCost']
        self.updateLists()
        '''self.animalsList.draw(window)'''

    def starve(self):
        for fauna in self.animalsList:
            if fauna.hunger == 0:
                self.animalsList.remove(fauna)
                self.peacocksList.remove(fauna)
                self.tigersList.remove(fauna)
                print(fauna, "died because of starvation")
        self.updateLists()

    def updateLists(self):
        self.animalsList.update()
        self.tigersList.update()
        self.peacocksList.update()

    def eat(self, PeacocksCollisionsList, TigersCollisionsList):
        for fauna in PeacocksCollisionsList:
            fauna.hunger += config.peacocks['eatingPoints']
        for fauna in TigersCollisionsList:
            fauna.hunger += config.tigers['eatingPoints']
        self.updateLists()

    def breed(self, window):
        for fauna in self.animalsList:
            if fauna.type == "peacock":
                if fauna.hunger >= config.peacocks['fertilityLvl']:
                    fauna.hunger -= config.peacocks['fertilityCost']
                    newone = Peacock()
                    newone.create()
                    self.peacocksList.add(newone)
                    self.animalsList.add(newone)

            elif fauna.type == "tiger":
                if fauna.hunger >= config.tigers['fertilityLvl']:
                    fauna.hunger -= config.tigers['fertilityCost']
                    newone = Tiger()
                    newone.create()
                    self.tigersList.add(newone)
                    self.animalsList.add(newone)

            self.updateLists()
            #self.animalsList.draw(window)
            #pygame.display.flip()

    def collide(self, PeacocksCollisionsList):
        for fauna in PeacocksCollisionsList:
            self.animalsList.remove(fauna)
            self.peacocksList.remove(fauna)
            print("Peacock eaten!")
        self.updateLists()


    def manageEvents(self, foodCollisionsList, PeacocksCollisionsList, TigersCollisionsList, window, window_rect, foodList):
        self.eat(foodCollisionsList, PeacocksCollisionsList)
        self.move(window, window_rect, foodList)
        self.eat(foodCollisionsList, TigersCollisionsList)
        self.starve()
        self.breed(window)

class Peacock(Animal):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pea.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.type = 'peacock'

    def create(self):
        self.weight = random.uniform(config.peacocks['minWeight'], config.peacocks['maxWeight'])
        self.speed = (config.peacocks['avgSpeed']*(4.5/self.weight))
        self.x = random.randint(1,100)
        self.y = random.randint(1,100)
        self.rect.x = self.x
        self.rect.y = self.y
        self.hunger = config.peacocks['startingHunger']



class Tiger(Animal):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/tig.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.type = 'tiger'

    def create(self):
        self.weight = random.uniform(config.tigers['minWeight'], config.tigers['maxWeight'])
        self.speed = (config.tigers['avgSpeed']*(182.5/self.weight))
        self.x = random.randint(600,700)
        self.y = random.randint(400,500)
        self.rect.x = self.x
        self.rect.y = self.y
        self.hunger = config.tigers['startingHunger']



    '''def eat(self, PeacocksCollisionsList):
        for tiger in PeacocksCollisionsList:
            tiger.hunger += config.tigers['eatingPoints']
            self.tigersList.update()'''
