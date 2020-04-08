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
        for tiger in range(config.animalsBeggining['startingTigersCount']):
            tiger=Tiger()
            tiger.create()
            self.animala.animalsList.add(tiger)
            #print (len(self.animala.animalsList))
        self.animala.animalsList.update()
        print (self.animala.animalsList)
        self.animala.animalsList.draw(self.window)
        pygame.display.flip()


        self.tour=0
        self.food_collision_list =pygame.sprite.Group()
        self.animals_collision_list =pygame.sprite.Group()

    def drawBackground(self):
        #background = pygame.image.load('background.jpg').convert()
        self.window.blit(self.background,(0,0))

    def detectCollisions(self):
        self.food_collision_list = pygame.sprite.groupcollide(self.animala.animalsList,self.fooda.foodList,False,pygame.sprite.collide_mask)
        self.animals_collision_list = pygame.sprite.groupcollide(self.animala.animalsList,self.animala.animalsList,False,pygame.sprite.collide_mask)


    def manageEvents(self):
        print (self.animala.animalsList)
        window = self.window
        window_rect = self.window_rect
        foodCollisionsList = self.food_collision_list
        AnimalCollisionsList = self.animals_collision_list
        foodList = self.fooda.foodList
        self.fooda.manageEventsFood(window, foodCollisionsList)
        self.detectCollisions()
        self.animala.manageEvents(foodCollisionsList, AnimalCollisionsList, window, window_rect, foodList)
