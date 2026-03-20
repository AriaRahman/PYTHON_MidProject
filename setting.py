import pygame 
from pygame.locals import *

screen_width = 800
screen_height= 650
screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SPACE SHOOTER")

#game_background=pygame.image.load()

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
pygame.quit()