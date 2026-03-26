from __future__ import annotations
import pygame 
from pygame import mixer
from utils import load_clean_image



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
bg = (255, 220, 0)
bgn = (200, 170, 0)
fg = (0, 0, 0)
enter_color=(0, 160, 0)
errcolor= (255, 80, 80)
quit_color = (180, 0, 0)




rows=4
columns= 6




game_background = pygame.image.load("images/space.jpg")

bullet_img = pygame.transform.scale(
    load_clean_image("images/bullet.png"), (40, 40))
spaceship_img = pygame.transform.scale(
    load_clean_image("images/spaceship.png"), (150, 70))
invader_bullet= pygame.transform.scale(
    load_clean_image("images/invaderbullet.png"), (20,20))



alien_cooldown = 1000
countdown= 3
game_over = 0 
last_count= pygame.time.get_ticks()
last_alien_shot = pygame.time.get_ticks()
time_now = pygame.time.get_ticks()

player_name = ""