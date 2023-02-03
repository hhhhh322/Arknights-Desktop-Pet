import pygame
import core.Button as Button
import sys
import re

def func():
    ...
pygame.init()
screen=pygame.display.set_mode((900,450))



while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()

