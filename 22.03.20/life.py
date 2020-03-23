### IMPORTING
import pygame
from tigers import Tiger
from peacocks import Peacock
from food import Food
import config


class Life():

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((config.screen['width'], config.screen['height']))
        self.window_rect = pygame.Rect((0, 0), (config.screen['width'], config.screen['height']))
        pygame.display.set_caption("Evolution of life")

        self.background = pygame.image.load('background.jpg').convert()

        self.peacocks = pygame.sprite.Group()
        self.tigers  = pygame.sprite.Group()
        self.food = pygame.sprite.Group()
        self.all_animals_list = pygame.sprite.Group()
        for i in range(config.animalsBeggining['startingPeacocksCount']):
            i=Peacock()
            i.create()
            self.peacocks.add(i)
        for j in range(config.animalsBeggining['startingTigersCount']):
            j=Tiger()
            j.create()
            self.tigers.add(j)

        self.all_animals_list.add(self.peacocks,self.tigers)
        self.tour=0
        self.food_collision_list =pygame.sprite.Group()
        self.animals_collision_list =pygame.sprite.Group()

    def drawBackground(self):
        background = pygame.image.load('background.jpg').convert()
        self.window.blit(self.background,(0,0))

    def manageMovement(self):
        # <- moving peacocks and tigers
        self.peacocks.update()
        self.tigers.update()
        self.all_animals_list.update()
        for i in self.all_animals_list:
            i.move(self.window_rect)

        # DETECTING COLLISIONS
        self.food_collision_list = pygame.sprite.groupcollide(self.peacocks,self.food,False,pygame.sprite.collide_mask)
        self.animals_collision_list = pygame.sprite.groupcollide(self.tigers,self.peacocks,False,pygame.sprite.collide_mask)
        self.peacocks.update()
        self.tigers.update()
        self.all_animals_list.update()
        self.all_animals_list.draw(self.window)

    def manageEventsFood(self):
        # <- managing food
        for k in range(config.food['startingFoodCount']):
            k=Food()
            k.create()
            self.food.add(k)
        self.food.update()
        self.food.draw(self.window)

        for i in self.food_collision_list:
            self.food.remove(self.food_collision_list[i])
            self.food.update()
        for i in self.food:
            if i.rotting() == True:
            # food durability
                self.food.remove(i)

    def manageEventsAnimals(self):
        for i in self.food_collision_list:
            i.hunger += config.peacocks['eatingPoints']
            self.peacocks.update()

        for i in self.peacocks:
            if i.starve() == True:
                self.peacocks.remove(i)
                self.peacocks.update()

        for i in self.peacocks:
            i.fertile()
            if i.fertilibity == True:
                print('nono')
                newone =i.breed()
                self.peacocks.add(newone)
                self.peacocks.update()
                self.all_animals_list.update()
                self.peacocks.draw(self.window)

        for i in self.tigers:
            if i.starve() == True:
                self.tigers.remove(i)
                self.tigers.update()
            #if i.fertile == True:

        for i in self.animals_collision_list:
            i.hunger+= config.tigers['eatingPoints']
            self.tigers.update()
            print("a")
            self.peacocks.remove(self.animals_collision_list[i])
            self.peacocks.update()
            print("b")

        self.all_animals_list.update()
        #self.all_animals_list.draw(self.window)
        print (len(self.peacocks))

    '''ef count(self):
        text = self._smallFont.render("Hello World!", 1, (10, 10, 10))
        window.blit(text, (50,50))'''
