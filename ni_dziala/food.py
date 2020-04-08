import pygame
import random
import config

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # setting pygame stuff
        self.image = pygame.image.load("images/apple.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.freshness = config.food['freshness']
        #self.flag = "food" <- not in use by now

        self.foodList = pygame.sprite.Group()


    def create(self, window):
        for food in range(config.food['startingFoodCount']):
            food=Food()
            food.x = random.randint(0,700)
            food.y = random.randint(0,500)
            self.foodList.add(food)
            food.rect.x = food.x
            food.rect.y = food.y
            food.localisation = dict(x = food.rect.x,
                y = food.rect.y)
        self.foodList.update()
        self.foodList.draw(window)

    def collide(self, foodCollisionsList):
        for food in foodCollisionsList:
            self.foodList.remove(food)
            self.foodList.update()

    def rotting(self):
        for food in self.foodList:
            food.freshness -=1
            if food.freshness == 0:
                self.foodList.remove(food)
                self.foodList.update()

    def manageEventsFood(self, window, foodCollisionsList):
        #food = Food()
        self.create(window)
        self.collide(foodCollisionsList)
        self.rotting()
