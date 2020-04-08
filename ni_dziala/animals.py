import pygame
import random
import config

class Animal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animalsList  = pygame.sprite.Group()

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
                '''if fauna.type == "peacock":
                    fauna.hunger -= config.peacocks['moveCost']
                elif fauna.type == "tiger":
                    fauna.hunger -= config.tiger['moveCost']'''
            else:
                pos = pygame.math.Vector2(peacock.x, peacock.y)
                if fauna.type == "peacock":
                    foodList = foodList
                elif fauna.type == "tiger":
                    foodList = []
                    for one in self.animalsList:
                        if one.type == "peacock":
                            foodList.add(one)

                food = min([food for food in foodList], key=lambda food: pos.distance_to(pygame.math.Vector2(food.x, food.y)))
                x = food.x
                y = food.y
                ###############
                if x > fauna.speed:
                    zwrotX = (x - fauna.x)
                    if zwrotX>0:
                        fauna.moveHor(1)
                    if zwrotX<0:
                        fauna.moveHor(-1)
                else:
                    # x < peacock.speed:
                    fauna.rect.x = x
                ###########
                if y > fauna.speed:
                    zwrotY = (y - fauna.y)
                    if zwrotY>0:
                        fauna.moveVer(1)
                    if zwrotY<0:
                        fauna.moveVer(-1)
                else:
                    # y < peacock.speed:
                    fauna.rect.y = y
                #peacock.moveVer(zwrotY)
            if fauna.type == "peacock":
                fauna.hunger -= config.peacocks['moveCost']
            elif fauna.type == "tiger":
                fauna.hunger -= config.tiger['moveCost']
        self.animalsList.update()
        self.animalsList.draw(window)

    def starve(self):
        for fauna in self.animalsList:
            if fauna.hunger == 0:
                self.animalsList.remove(fauna)
                self.animalsList.update()

    def foodFinding(self, foodList):
        for fauna in self.animalsList:
            pos = pygame.math.Vector2(fauna.x, fauna.y)
            food = min([food for food in foodList], key=lambda food: pos.distance_to(pygame.math.Vector2(food.x, food.y)))
            print(food.x)

    def eat(self, foodCollisionsList, AnimalCollisionsList):
        for fauna in self.animalsList:
            if fauna.type == "peacock":
                for fauna in foodCollisionsList:
                    fauna.hunger += config.peacocks['eatingPoints']
            elif fauna.type == "tiger":
                for fauna in AnimalCollisionsList:
                    fauna.hunger += config.tigers['eatingPoints']
            self.animalsList.update()

    def breed(self, window):
        for fauna in self.animalsList:
            if fauna.type == "peacock":
                if peacock.hunger >= config.peacocks['fertilityLvl']:
                    newone = Peacock()
                    newone.create(window)
                    self.animalsList.add(newone)

            elif fauna.type == "tiger":
                if tiger.hunger >= config.tigers['fertilityLvl']:
                    newone = Tiger()
                    newone.create(window)
                    self.tigersList .add(newone)

            self.animalsList.update()
            self.animalsList.draw(window)
            pygame.display.flip()

    def collide(self, AnimalCollisionsList):
        for fauna in AnimalcollisionsList:
            if fauna.type == "peacock":
                self.animalsList.remove(fauna)

        self.animalsList.update()


    def manageEvents(self, foodCollisionsList, AnimalCollisionsList, window, window_rect, foodList):
        self.eat(foodCollisionsList, AnimalCollisionsList)
        self.move(window, window_rect, foodList)
        self.eat(foodCollisionsList, AnimalCollisionsList)
        self.starve()
        self.breed(window)

class Peacock(pygame.sprite.Sprite):
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



class Tiger(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/tig.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #self.tigersList  = pygame.sprite.Group()
        self.type = 'tiger'

    def create(self):
        self.weight = random.uniform(config.tigers['minWeight'], config.tigers['maxWeight'])
        self.speed = (config.tigers['avgSpeed']*(182.5/self.weight))
        self.x = random.randint(600,700)
        self.y = random.randint(400,500)
        self.rect.x = self.x
        self.rect.y = self.y
        self.hunger = config.tigers['startingHunger']



    '''def eat(self, AnimalCollisionsList):
        for tiger in AnimalCollisionsList:
            tiger.hunger += config.tigers['eatingPoints']
            self.tigersList.update()'''
