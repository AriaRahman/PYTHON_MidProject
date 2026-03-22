import pygame 
from pygame.locals import *


clock = pygame.time.Clock()
fps=60


screen_width = 1060
screen_height= 700
screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SPACE SHOOTER")


red= (255,0,0)
green= (0,255,0)
game_background=pygame.image.load("images/space.jpg")


def load_clean_image(path, remove_white=True):
    img = pygame.image.load(path).convert_alpha()
    if remove_white:
        width, height = img.get_size()
        for x1 in range(width):
            for y1 in range(height):
                r, g, b, a = img.get_at((x1, y1))
                if r > 200 and g > 200 and b > 200:
                    img.set_at((x1, y1), (0, 0, 0, 0))
    return img


bullet_img = pygame.transform.scale(load_clean_image("images/bullet.png"), (50, 50))
spaceship_img = pygame.transform.scale(load_clean_image("images/spaceship.png"), (150, 70))
alien_img  = pygame.transform.scale(load_clean_image("images/alien" + str(random.radiant(1 ,5)) + ".png"), (150, 70))




def draw_bg():
    screen.blit(game_background,(0,0))



class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = spaceship_img.copy()   
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()
    

 
    def update(self):
        speed = 8
        cooldown = 100
        key= pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += speed


        time_now = pygame.time.get_ticks()
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            bullet = Bullets(self.rect.centerx , self.rect.top)
            bullet_group.add(bullet)
            self.last_shot= time_now




        pygame.draw.rect(screen, red, (self.rect.x , (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0 :
                 pygame.draw.rect(screen,green , (self.rect.x , (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining/ self.health_start)), 15))



# class Bullets(pygame.sprite.Sprite):
#     def __init__(self, x,y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load("images/bullet.png")
#         self.rect = self.image.get_rect()
#         self.rect.midbottom = (x, y)

#     def update(self):
#         self.rect.y -= 5
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img.copy()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    def update(self):
        self.rect.y -= 11
        if self.rect.bottom < 0:
            self.kill()
  

class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img.copy()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)






spaceship_group = pygame.sprite.Group()
bullet_group= pygame.sprite.Group()

spaceship= Spaceship(int(screen_width / 2),screen_height - 100 , 3)
spaceship_group.add(spaceship)


run=True
while run:
    clock.tick(fps)
    draw_bg()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False


    spaceship.update() 
    bullet_group.update()




    spaceship_group.draw(screen)
    bullet_group.draw(screen)



    pygame.display.update()
pygame.quit()