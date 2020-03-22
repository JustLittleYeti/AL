### IMPORTING
import pygame
from tigers import Tiger
from peacocks import Peacock
from food import Food


class Life():

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Evolution of life")
        self.background = pygame.image.load('background.jpg').convert()
        self._smallFont = pygame.font.SysFont('calibri',30)
        self._bigFont = pygame.font.SysFont('calibri', 80)
        self.peacocks = Peacock()
        self.tigers = Tiger()
        self.food = Food()
        self.tour=0

    def drawBackground(self):
        self.window.blit(self._background,(0,0))

    def manageEventspeacockf(self, food_collision_list):
        for i in food_collision_list:
            if i == Peacock():
                i.eat(food_collision_list)
                i.starve()

    def manageEventsTiger(self,animals_collision_list):
        for i in animals_collision_list:
            if i == Tiger():
                i.eat(animals_collision_list)
                i.starve()

    def manageMovement(self, animal):
        # <- moving peacocks and tigers
        for i in animal:
            i.move()

    def manageEventsFood(self,food_collision_list,food):
        # <- managing food
        self.food.create(food)

        for i in food_collision_list:
            if i == Food():
                i.be_eaten(food_collision_list)
        for i in food:
            i.rotting()
            i.dissapear()

    '''def count(self):
        text = self._smallFont.render("Tour: ",self.tour, True,(255,255,255))
        self._window.blit(text,(50,360))'''
#"Tigers: %d"%self.tigers.getCounter(), True,(200,200,200)
