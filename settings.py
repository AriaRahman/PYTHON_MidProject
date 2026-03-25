from __future__ import annotations
import pygame 
from pygame import mixer



pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()



screen_width = 1060
screen_height= 700
screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SPACE SHOOTER")


clock = pygame.time.Clock()
fps=60


font30= pygame.font.SysFont('Constantia', 30)
font40= pygame.font.SysFont('Constantia', 40)



explosion_fx = pygame.mixer.Sound("images/explosion.wav")
explosion_fx.set_volume(0.25)

explosion2_fx = pygame.mixer.Sound("images/explosion2.wav")
explosion2_fx.set_volume(0.25)

laser_fx = pygame.mixer.Sound("images/laser.wav")
laser_fx.set_volume(0.25)


red= (255,0,0)
green= (0,255,0)
white= (255,255,255)



rows=4
columns= 5



alien_cooldown = 1000
countdown= 3
game_over = 0 
last_count= pygame.time.get_ticks()
last_alien_shot = pygame.time.get_ticks()
time_now = pygame.time.get_ticks()

