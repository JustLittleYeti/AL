import pygame
import random
import config
import math

class Animal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animalsList  = pygame.sprite.Group()
        self.peacocksList  = pygame.sprite.Group()
        self.tigersList  = pygame.sprite.Group()

    def breed(self, window):
        for fauna in self.animalsList:
            if fauna.hunger >= fauna.fertilityLvl:
                fauna.hunger -= fauna.fertilityCost
                newone = fauna.returnClass()
                newone.create()
                self.animalsList.add(newone)
                if fauna.type == "peacock":
                    self.peacocksList.add(newone)
                elif fauna.type == "tiger":
                    self.tigersList.add(newone)
        self.updateLists()

    def collide(self, PeacocksCollisionsList):
        for fauna in PeacocksCollisionsList:
            self.animalsList.remove(fauna)
            self.peacocksList.remove(fauna)
            print("Peacock eaten!")
        self.updateLists()

    def eat(self, PeacocksCollisionsList, TigersCollisionsList):
        for fauna in PeacocksCollisionsList:
            fauna.hunger += fauna.eatingPoints
        for fauna in TigersCollisionsList:
            fauna.hunger += fauna.eatingPoints
        self.updateLists()

    def lookForFood(self, dist, window_rect):
        food = dist
        if food.rect.x > self.speed:
            directionX = (food.rect.x - self.rect.x)
            if directionX>0:
                self.moveHor(1, window_rect)
            if directionX<0:
                self.moveHor(-1, window_rect)
        else:
            # x < speed:
            self.rect.x = food.rect.x
        if food.rect.y > self.speed:
            directionY = (food.rect.y - self.rect.y)
            if directionY>0:
                self.moveVer(1, window_rect)
            if directionY<0:
                self.moveVer(-1, window_rect)
        else:
            # y < speed:
            self.rect.y = food.rect.y
        self.hunger -= self.moveCost

    def moveHor(self, direction, window_rect):
        move_horizontal=direction*self.speed
        self.rect.x += move_horizontal
        self.rect.clamp_ip(window_rect)

    def moveVer(self, direction, window_rect):
        move_vertical=direction*self.speed
        self.rect.y += move_vertical
        self.rect.clamp_ip(window_rect)

    def move(self, window, window_rect, ListP, ListT):
        for fauna in self.animalsList:
            if fauna.hunger>=fauna.fertilityLvl:
                fauna.breed(window)
            elif fauna.hunger<=fauna.hungerPoint:
                dist=fauna.detectFood(ListP, ListT)
                if not dist == []:
                    fauna.lookForFood(dist, window_rect)
                else
                    fauna.randoMove()
            else:
                fauna.randoMove(window_rect)
        self.updateLists()

    def randoMove(self,window_rect):
        option=[-1,1]
        self.moveHor(random.choice(option), window_rect)
        self.moveVer(random.choice(option), window_rect)
        self.hunger -= self.moveCost

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


    def manageEvents(self, foodCollisionsList, PeacocksCollisionsList, TigersCollisionsList, window, window_rect, ListP, ListT):
        self.eat(foodCollisionsList, PeacocksCollisionsList)
        self.collide(PeacocksCollisionsList)
        self.move(window, window_rect, ListP, ListT)
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
        self.maxCount = config.peacocks['maxCount']
        self.minHungerPeace = config.peacocks['minHungerPeace']
        self.maxHungerPeace = config.peacocks['maxHungerPeace']
        self.minHunger = config.peacocks['minHunger']
        self.maxHunger = config.peacocks['maxHunger']
        self.eatingPoints = config.peacocks['eatingPoints']
        self.moveCost = config.peacocks['moveCost']
        self.startingHunger = config.peacocks['startingHunger']
        self.hungerPoint = config.peacocks['hungerPoint']
        self.minWeight = config.peacocks['minWeight']
        self.maxWeight = config.peacocks['maxWeight']
        self.avgSpeed = config.peacocks['avgSpeed']
        self.fertilityLvl = config.peacocks['fertilityLvl']
        self.fertilityCost = config.peacocks['fertilityCost']
        self.minEggCount = config.peacocks['minEggCount']
        self.maxEggCount = config.peacocks['maxEggCount']
        #self.foodList = config.peacocks['foodList']

    def create(self):
        self.weight = random.uniform(self.minWeight, self.maxWeight)
        self.speed = (self.avgSpeed*(4.5/self.weight))
        self.x = random.randint(1,100)
        self.y = random.randint(1,100)
        self.rect.x = self.x
        self.rect.y = self.y
        self.hunger = self.startingHunger

    def returnClass(self):
        return Peacock()

    def detectFood(self,ListP, ListT):
        foodList = ListP
        pos = pygame.math.Vector2(self.rect.x, self.rect.y)
        nearestFood=min([food for food in foodList], key=lambda food: pos.distance_to(pygame.math.Vector2(food.rect.x, food.rect.y)))
        return nearestFood



class Tiger(Animal):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/tig.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.type = 'tiger'
        self.maxCount = config.tigers['maxCount']
        self.minHungerPeace = config.tigers['minHungerPeace']
        self.maxHungerPeace = config.tigers['maxHungerPeace']
        self.minHunger = config.tigers['minHunger']
        self.maxHunger = config.tigers['maxHunger']
        self.eatingPoints = config.tigers['eatingPoints']
        self.moveCost = config.tigers['moveCost']
        self.startingHunger = config.tigers['startingHunger']
        self.hungerPoint = config.tigers['hungerPoint']
        self.minWeight = config.tigers['minWeight']
        self.maxWeight = config.tigers['maxWeight']
        self.avgSpeed = config.tigers['avgSpeed']
        self.fertilityLvl = config.tigers['fertilityLvl']
        self.fertilityCost = config.tigers['fertilityCost']
        self.minCubCount = config.tigers['minCubCount']
        self.maxCubCount = config.tigers['maxCubCount']

    def create(self):
        self.weight = random.uniform(self.minWeight, self.maxWeight)
        self.speed = (self.avgSpeed*(182.5/self.weight))
        self.x = random.randint(600,700)
        self.y = random.randint(400,500)
        self.rect.x = self.x
        self.rect.y = self.y
        self.hunger = self.startingHunger

    def returnClass(self):
        return Tiger()

    def detectFood(self, ListP, ListT):
        foodList = ListT
        pos = pygame.math.Vector2(self.x, self.y)
        nearestFood=min([food for food in foodList], key=lambda food: pos.distance_to(pygame.math.Vector2(food.rect.x, food.rect.y)))
        print(self, "nearest food: ", nearestFood.rect.x, nearestFood.rect.y)
        return nearestFood
