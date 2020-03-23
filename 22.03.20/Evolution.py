### IMPORTING
import pygame
from life import Life
import config


### BASICS
tour=0
life=Life()
run = True
clock = pygame.time.Clock()




while run:
    # --- Main event loop
    life.drawBackground()
    pygame.time.delay(config.delay)

    for event in pygame.event.get():

        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            run = False
        elif keys[pygame.K_ESCAPE]:
            run = False
        elif keys[pygame.K_SPACE]:
            pygame.time.delay(5000)
            # nie dziala
    life.manageMovement()
    life.manageEventsFood()
    life.manageEventsAnimals()




    pygame.display.flip()

    clock.tick(config.FPS)
    #FPS

    print('Tour: ', tour)
    tour+=1

pygame.quit()
