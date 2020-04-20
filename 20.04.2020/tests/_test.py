import pytest
import pygame

class FoodTests():

    def create(self, foodList, window):
        for food in range(config.food['startingFoodCount']):
            food=Food()
            food.x = random.randint((config.screen['width'], config.screen['height']))
            food.y = random.randint((config.screen['width'], config.screen['height']))
            foodList.food.add(food)
        foodList.update()
        foodList.draw(window)


    def collide(self, foodList, collisionsList):
        for food in collisionsList:
            foodList(collisionsList[food])
            foodList.update()

    def rotting(self, foodList):
        for food in foodList:
            if self.freshness == 0:
                foodList.remove(food)
                foodList.update()

    def manageEventsFood(self, list, window, collisionsList):
        create(list)
        collide(list, window)
        rotting(foodList)
