### IMPORTING
import pygame
from peacocks import Peacock
from life import Life
from tigers import Tiger
from food import Food

#life = life.Life()
pygame.init()


### BASICS
tour=1
life=Life()
run = True
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
size = (700, 500)

screen = pygame.display.set_mode(size)
background = pygame.image.load('background.jpg').convert()

### - CREATING ANIMALS AND FOOD
peacocks = pygame.sprite.Group()
tigers  = pygame.sprite.Group()
food = pygame.sprite.Group()
all_animals_list = pygame.sprite.Group()

for i in range(10):
    i=Peacock()
    i.create()
    peacocks.add(i)
for j in range(10):
    j=Tiger()
    j.create()
    tigers.add(j)

all_animals_list.add(peacocks,tigers)


### COLLISIONS LISTS


while run:
    # --- Main event loop

    screen.blit(background,(0,0))
    pygame.time.delay(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif keys[pygame.K_ESCAPE]:
            run = False
            # nie dziala


    food_collision_list = pygame.sprite.groupcollide(peacocks,food,False,pygame.sprite.collide_mask)
    animals_collision_list = pygame.sprite.groupcollide(tigers,peacocks,False,pygame.sprite.collide_mask)

    food.update()
    life.manageEventsFood(food_collision_list, food)
    #life.count()
    food.draw(screen)
    pygame.display.flip()

    life.manageEventspeacockf(food_collision_list)
    life.manageEventsTiger(animals_collision_list)
    life.manageMovement(all_animals_list)
    all_animals_list.update()
    all_animals_list.draw(screen)
    pygame.display.flip()

    clock.tick(60)
    #FPS

    print('Tour: ', tour)
    tour+=1

pygame.quit()
