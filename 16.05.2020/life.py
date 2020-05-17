import pygame
from animals import Animal,Peacock,Tiger
from food import Food
import config


class Life():

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((config.screen['width'], config.screen['height']))
        self.window_rect = pygame.Rect((0, 0), (config.screen['width'], config.screen['height']))
        pygame.display.set_caption("Evolution of life")

        self.background = pygame.image.load('images/background.jpg').convert()

        self.fooda = Food()
        self.animala = Animal()

        for peacock in range(config.animalsBeggining['startingPeacocksCount']):
            peacock=Peacock()
            peacock.create()
            self.animala.animalsList.add(peacock)
            self.animala.peacocksList.add(peacock)
        for tiger in range(config.animalsBeggining['startingTigersCount']):
            tiger=Tiger()
            tiger.create()
            self.animala.animalsList.add(tiger)
            self.animala.tigersList.add(tiger)

        self.tour=0
        self.food_collision_list =pygame.sprite.Group()
        self.peacocks_collision_list =pygame.sprite.Group()
        self.tigers_collision_list =pygame.sprite.Group()

    def drawBackground(self):
        #background = pygame.image.load('background.jpg').convert()
        self.window.blit(self.background,(0,0))

    def drawAnimals(self):
        self.animala.animalsList.update()
        self.animala.animalsList.draw(self.window)
        pygame.display.flip()

    def detectCollisions(self):
        self.food_collision_list = pygame.sprite.groupcollide(self.animala.peacocksList, self.fooda.foodList, False, pygame.sprite.collide_mask)
        self.peacocks_collision_list = pygame.sprite.groupcollide(self.animala.tigersList, self.animala.peacocksList, False, pygame.sprite.collide_mask)
        self.tigers_collision_list = pygame.sprite.groupcollide(self.animala.tigersList, self.animala.peacocksList, False, pygame.sprite.collide_mask)
        print (self.peacocks_collision_list, self.tigers_collision_list)

    def manageEvents(self):
        window = self.window
        window_rect = self.window_rect
        foodCollisionsList = self.food_collision_list
        PeacocksCollisionsList = self.peacocks_collision_list
        TigersCollisionsList = self.tigers_collision_list
        ListP = self.fooda.foodList
        ListT = self.animala.peacocksList
        self.fooda.manageEventsFood(window, foodCollisionsList)
        self.drawAnimals()
        self.detectCollisions()
        self.animala.manageEvents(foodCollisionsList, PeacocksCollisionsList, TigersCollisionsList, window, window_rect, ListP, ListT)
        print("Tigers: ", self.animala.tigersList)
        print("Peacocks: ", self.animala.peacocksList)
        self.tour +=1
        self.test()

    def test(self):
        with open ("output.txt", "a") as file:
            a,b = 1,1
            print("\nTOUR: ", self.tour, "\n", file=file)
            file.write("PEACOCKS: \n")
            for peacock in self.animala.peacocksList:
                print("Peacock", a, "Hunger: ", peacock.hunger, "Position: ", peacock.x, peacock.y, file=file)
                a+=1
            file.write("\nTIGERS: \n")
            for tiger in self.animala.tigersList:
                print("Tiger", b, "Hunger: ", tiger.hunger, "Position: ", tiger.x, tiger.y, file=file)
                b+=1
                tiger.introduceSelf()
