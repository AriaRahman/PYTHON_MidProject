import pygame 
from pygame.locals import *
import random


clock = pygame.time.Clock()
fps=60


screen_width = 1060
screen_height= 700
screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SPACE SHOOTER")



rows=5
columns= 5
alien_cooldown = 1000
last_alien_shot = pygame.time.get_ticks()


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


bullet_img = pygame.transform.scale(load_clean_image("images/bullet.png"), (40, 40))
spaceship_img = pygame.transform.scale(load_clean_image("images/spaceship.png"), (150, 70))
invader_bullet= pygame.transform.scale(load_clean_image("images/invaderbullet.png"), (20,20))



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
        cooldown = 250
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

        

        self.mask = pygame.mask.from_surface(self.image)






        pygame.draw.rect(screen, red, (self.rect.x , (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0 :
                 pygame.draw.rect(screen,green , (self.rect.x , (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining/ self.health_start)), 15))
        elif self.health_remaining <=0:
            explosion= Explosion (self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)
            self.kill()


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
        if pygame.sprite.spritecollide(self, alien_group, True):
            self.kill()
            explosion= Explosion (self.rect.centerx, self.rect.centery, 2)
            explosion_group.add(explosion)
  

# class Aliens(pygame.sprite.Sprite):
#     move_direction=1
#     move_counter=0
    
#     def __init__(self, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         alien_img  = pygame.transform.scale(load_clean_image("images/alien" + str(random.randint(1 ,5)) + ".png"), (65, 70))
#         self.image = alien_img.copy()
#         self.rect = self.image.get_rect()
#         self.rect.midbottom = (x, y)

#         # self.move_counter = 0 
#         # self.move_direction = 1 
    
#     def update(self):
#         self.rect.x += Aliens.move_direction

#         if self == list (alien_group)[0]:
#             Aliens.move_counter += 1
       
#        # self.move_counter += 1

#             if Aliens.move_counter >= 200 :
#                Aliens.move_direction *= -1
#                Aliens.move_counter = 0

class Aliens(pygame.sprite.Sprite):
    move_direction = 1
    should_flip = False 

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        alien_img = pygame.transform.scale(
            load_clean_image("images/alien" + str(random.randint(1, 5)) + ".png"), (60, 60)
        )
        self.image = alien_img.copy()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    def update(self):
        self.rect.x += Aliens.move_direction

        if self.rect.right >= screen_width or self.rect.left <= 0:
            Aliens.should_flip = True

        if self == list(alien_group)[-1]:
            if Aliens.should_flip:
                Aliens.move_direction *= -1
                Aliens.should_flip = False     




class Alien_Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = invader_bullet.copy()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    def update(self):
        self.rect.y += 4
        if self.rect.top > screen_height:
            self.kill()
        
        if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask):
            self.kill()
            spaceship.health_remaining -= 1
            explosion= Explosion (self.rect.centerx, self.rect.centery, 1)
            explosion_group.add(explosion)







class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)

        self.images=[]
        for num in range(1,6):
            img = pygame.image.load(f"images/exp{num}.png")
            
            if size == 1 :
                img = pygame.transform.scale(img, (20,20))
            
            if size == 2 :
                img = pygame.transform.scale(img, (40,20))
            
            if size == 3 :
                img = pygame.transform.scale(img, (150,150))

            self.images.append(img)
        

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.counter = 0

    def update(self):
        explosion_speed = 3
        self.counter += 1
        
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter=0
            self.index  +=1
            self.image = self.images[self.index]

        
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()





spaceship_group = pygame.sprite.Group()
bullet_group= pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
explosion_group= pygame.sprite.Group()

total_width = (columns - 1) * 130  
start_x = (screen_width - total_width) // 2

def create_aliens():
    for row in range(rows):
        for item in range(columns):
            alien= Aliens(start_x + item * 130, 100 + row * 75)
            alien_group.add(alien)


create_aliens()


spaceship= Spaceship(int(screen_width / 2),screen_height - 100 , 3)
spaceship_group.add(spaceship)


run=True
while run:
    clock.tick(fps)
    draw_bg()

    time_now = pygame.time.get_ticks()


    if time_now - last_alien_shot > alien_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0 :
          attacking_alien = random.choice (alien_group.sprites())
          alien_bullet = Alien_Bullets (attacking_alien.rect.centerx, attacking_alien.rect.bottom)
          alien_bullet_group.add(alien_bullet)
          last_alien_shot = time_now



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False


    spaceship.update() 

    bullet_group.update()
    alien_group.update()
    alien_bullet_group.update()
    explosion_group.update()




    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)
    alien_bullet_group.draw(screen)
    explosion_group.draw(screen)



    pygame.display.update()
pygame.quit()