import pygame
from life import Life
import config

### BASICS
tour=0
life=Life()
run = True
clock = pygame.time.Clock()

while run:
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

    life.manageEvents()

    pygame.display.flip()

    clock.tick(config.FPS)
    #FPS
    tour+=1
    print('Tour: ', tour)


pygame.quit()
