
"""
Defines all game objects as Pygame sprites:
- Spaceship  : player-controlled ship (movement, shooting, health)
- Bullets    : player projectiles
- Aliens     : shared formation movement)
- Alien_Bullets : enemy projectiles   
- Explosion  : animated sprite-sheet effect
- MenuButton : reusable UI button
- Heart      : increases player-controlled ship's health 

"""

from __future__ import annotations

import random
import pygame

import settings 

from utils import load_clean_image


class Spaceship(pygame.sprite.Sprite):
    
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = settings.spaceship_img.copy()   
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()
    

 
    def update(self):
        speed = 3
        cooldown = 500
        game_over= 0

        key= pygame.key.get_pressed()

        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed

        if key[pygame.K_RIGHT] and self.rect.right < settings.screen_width:
            self.rect.x += speed

        if key[pygame.K_SPACE] and settings.time_now - self.last_shot > cooldown:
            settings.laser_fx.play()
            bullet = Bullets(self.rect.centerx , self.rect.top)
            bullet_group.add(bullet)
            self.last_shot= settings.time_now

        

        self.mask = pygame.mask.from_surface(self.image)

        pygame.draw.rect(settings.screen, settings.red, (self.rect.x , (self.rect.bottom + 10), self.rect.width, 15))
       
       
        if self.health_remaining > 0 :
                 
                 pygame.draw.rect(settings.screen,settings.green , 
                                  (self.rect.x , (self.rect.bottom + 10), 
                                   int(self.rect.width * (self.health_remaining/ self.health_start)), 15))
       
       
        elif self.health_remaining <=0:

            explosion= Explosion (self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)
            self.kill()
            game_over = -1

        return game_over



class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = settings.bullet_img.copy()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    def update(self):
        self.rect.y -= 11
        if self.rect.bottom < 0:
            self.kill()
        # if pygame.sprite.spritecollide(self, alien_group, True):
        #     self.kill()
        #     settings.score +=10
        #     settings.explosion_fx.play()
        #     explosion= Explosion (self.rect.centerx, self.rect.centery, 2)
        #     explosion_group.add(explosion)
        hits = pygame.sprite.spritecollide(self, alien_group, False)
        if hits:
             #self.kill()
        
             alien = hits[0] 
             alien.health -= 1
             self.kill()
             if alien.health <= 0:
                  
                  alien.kill()
                  settings.score += 10
                  settings.explosion_fx.play()
                  explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
                  explosion_group.add(explosion)

                  if settings.score % 30 == 0:
                      heart = Heart(alien.rect.centerx, alien.rect.centery)
                      heart_group.add(heart)


             else:
         
                  alien.image.set_alpha(130)



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
        self.health = 3

    def update(self):
        self.rect.x += Aliens.move_direction

        if self.rect.right >= settings.screen_width or self.rect.left <= 0:
            Aliens.should_flip = True

        if self == list(alien_group)[-1]:

            if Aliens.should_flip:

                Aliens.move_direction *= -1
                Aliens.should_flip = False     




class Alien_Bullets(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = settings.invader_bullet.copy()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    def update(self):
        self.rect.y += 4
        if self.rect.top > settings.screen_height:
            self.kill()
        
        if pygame.sprite.spritecollide(self, spaceship_group, False, 
                                       pygame.sprite.collide_mask):
           
            self.kill()
            settings.explosion2_fx.play()
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
        explosion_speed = 6
        self.counter += 1
        
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter=0
            self.index  +=1
            self.image = self.images[self.index]

        
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()


class MenuButton:
 
    def __init__(self, cx, cy, w, h, label, enabled=True, color = None):
        self.rect    = pygame.Rect(0, 0, w, h)
        self.rect.center = (cx, cy)
        self.label   = label
        self.enabled = enabled
        self.color = color
 
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.enabled and self.rect.collidepoint(event.pos):
                return True
        return False
 
    def draw(self, surf):
        hovered = self.rect.collidepoint(pygame.mouse.get_pos()) and self.enabled
 
        base= self.color if self.color else settings.bg 
        r,g,b = base
        bg = (min(r + 40, 255), min(g + 40, 255), 
              min(b + 40, 255)) if hovered else base
       

        pygame.draw.rect(surf, bg, self.rect)
        pygame.draw.rect(surf, settings.fg, self.rect, 2)
 
        label_surf = settings.font30.render(self.label, True, settings.fg)
        surf.blit(label_surf, label_surf.get_rect(center=self.rect.center))


class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(load_clean_image("images/heart.png"), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += 3
        if self.rect.top > settings.screen_height:
            self.kill()
        
        if pygame.sprite.spritecollide(self, spaceship_group, False):
            self.kill()
            if spaceship:
                spaceship.health_remaining = min(spaceship.health_remaining + 1, spaceship.health_start)





spaceship_group = pygame.sprite.Group()
bullet_group= pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
explosion_group= pygame.sprite.Group()
heart_group = pygame.sprite.Group()


total_width = (settings.columns - 1) * 130  
start_x = (settings.screen_width - total_width) // 2

def create_aliens():
    for row in range(settings.rows):
        for item in range(settings.columns):
            alien= Aliens(start_x + item * 130, 100 + row * 75)
            alien_group.add(alien)




spaceship: Spaceship | None =   None

def create_spaceship() -> Spaceship:
    global spaceship

    spaceship= Spaceship(int(settings.screen_width / 2),
                     settings.screen_height - 100 , 3)

    spaceship_group.add(spaceship)
    return spaceship
