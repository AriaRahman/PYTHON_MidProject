import pygame 
from pygame.locals import *


clock = pygame.time.Clock()
fps=60


screen_width = 1000
screen_height= 700
screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SPACE SHOOTER")

game_background=pygame.image.load("images/space.jpg")


def draw_bg():
    screen.blit(game_background,(0,0))

run=True
while run:
    clock.tick(fps)
    draw_bg()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False


    pygame.display.update()
pygame.quit()