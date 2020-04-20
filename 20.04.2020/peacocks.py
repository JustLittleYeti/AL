import pygame
import random
import config

class Peacock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pea.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.peacocksList = pygame.sprite.Group()


    def create(self, window):
        self.weight = random.uniform(config.peacocks['minWeight'], config.peacocks['maxWeight'])
        self.speed = (config.peacocks['avgSpeed']*(4.5/self.weight))
        self.x = random.randint(1,100)
        self.y = random.randint(1,100)
        self.rect.x = self.x
        self.rect.y = self.y
        self.hunger = config.peacocks['startingHunger']
        self.peacocksList.update()
        self.peacocksList.draw(window)

    def moveHor(peacock, zwrot):
        move_horizontal=zwrot*peacock.speed
        peacock.rect.x += move_horizontal

    def moveVer(peacock, zwrot):
        move_vertical=zwrot*peacock.speed
        peacock.rect.y += move_vertical

    def move(self, window, window_rect,foodList):
        # <- movement
        option=[-1,1]
        '''abba = random.choice(option)
        baab = random.choice(option)'''
        for peacock in self.peacocksList:
            if peacock.hunger >= 50:
                peacock.moveHor(random.choice(option))
                peacock.moveVer(random.choice(option))
                peacock.rect.clamp_ip(window_rect)
                peacock.hunger -= config.peacocks['moveCost']
            else:
                pos = pygame.math.Vector2(peacock.x, peacock.y)
                food = min([food for food in foodList], key=lambda food: pos.distance_to(pygame.math.Vector2(food.x, food.y)))
                x = food.x
                y = food.y
                ###############
                if x > peacock.speed:
                    zwrotX = (x - peacock.x)
                    if zwrotX>0:
                        peacock.moveHor(1)
                    if zwrotX<0:
                        peacock.moveHor(-1)
                else:
                    # x < peacock.speed:
                    peacock.rect.x = x
                ###########
                if y > peacock.speed:
                    zwrotY = (y - peacock.y)
                    if zwrotY>0:
                        peacock.moveVer(1)
                    if zwrotY<0:
                        peacock.moveVer(-1)
                else:
                    # y < peacock.speed:
                    peacock.rect.y = y
                #peacock.moveVer(zwrotY)
                peacock.hunger -= config.peacocks['moveCost']

        self.peacocksList.update()
        self.peacocksList.draw(window)

    def eat(self, foodCollisionsList):
        for peacock in foodCollisionsList:
            peacock.hunger += config.peacocks['eatingPoints']
            self.peacocksList.update()

    def starve(self):
        for peacock in self.peacocksList:
            if peacock.hunger == 0:
                peacocksList.remove(peacock)
                peacocksList.update()

    def breed(self, window):
        for peacock in self.peacocksList:
            if peacock.hunger >= config.peacocks['fertilityLvl']:

                newone = Peacock()
                newone.create(window)
                self.peacocksList.add(newone)
                self.peacocksList.update()
                #self.all_animals_list.update()
                self.peacocksList.draw(window)

    def collide(self, AnimalCollisionsList):
        for peacock in AnimalcollisionsList:
            self.peacocksList.remove(peacock)
            self.peacocksList.update()

    def foodFinding(self, foodList):
        for peacock in self.peacocksList:
            pos = pygame.math.Vector2(peacock.x, peacock.y)
            food = min([food for food in foodList], key=lambda food: pos.distance_to(pygame.math.Vector2(food.x, food.y)))
            print(food.x)
            #return food



    def manageEventsPeacocks(self, foodCollisionsList, AnimalCollisionsList, window, window_rect, foodList):
        print("Peacocks: ", len(self.peacocksList))
        self.eat(foodCollisionsList)
        self.move(window, window_rect, foodList)
        self.eat(foodCollisionsList)
        self.starve()
        self.breed(window)
