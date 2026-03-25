from __future__ import annotations

import random
import pygame
import settings
from utils import draw_bg, draw_text

from entities import (
    MenuButton,
    Alien_Bullets,
    spaceship_group,
    bullet_group,
    alien_group,
    alien_bullet_group,
    explosion_group,
    create_aliens,
    create_spaceship,
)
cx = settings.screen_width  // 2
cy = settings.screen_height // 2


def run_menu() -> bool:
   
 
    btn_player = MenuButton(cx, cy - 80, 300, 50, "PLAYER NAME",  enabled=False)
    btn_start  = MenuButton(cx, cy,      300, 50, "START GAME",   enabled=True)
    btn_scores = MenuButton(cx, cy + 80, 300, 50, "HIGH SCORES",  enabled=False)
 
    buttons = [btn_player, btn_start, btn_scores]
 
    while True:
        settings.clock.tick(settings.fps)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            for btn in buttons:
                if btn.handle_event(event):
                    if btn is btn_start:
                        return True
 
        draw_bg()
 
        draw_text('SPACE SHOOTER', settings.font40, settings.white,
                  cx - 150, cy - 200)
 
        for btn in buttons:
            btn.draw(settings.screen)
 
        pygame.display.update()


def show_instructions() -> bool:
 
    while True:
        settings.clock.tick(settings.fps)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return True
 
        draw_bg()
 
        draw_text('HOW TO PLAY',         settings.font40, settings.white, cx - 110, cy - 160)
        draw_text('< >   Move left / right', settings.font30, settings.white, cx - 160, cy - 60)
        draw_text('SPACE   Shoot',           settings.font30, settings.white, cx - 160, cy)
        draw_text('Press ENTER to start',    settings.font30, settings.white, cx - 160, cy + 100)
 
        pygame.display.update()
 




def rungame() -> None:
    create_aliens()
    spaceship= create_spaceship()


    run= True

    while run:
        settings.clock.tick(settings.fps)
        settings.time_now = pygame.time.get_ticks()

        draw_bg()
  
        if settings.countdown == 0 : 

   
             if settings.time_now - settings.last_alien_shot > settings.alien_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0 :
        
                attacking_alien = random.choice (alien_group.sprites())
                alien_bullet = Alien_Bullets (attacking_alien.rect.centerx, 
                                         attacking_alien.rect.bottom)
            
                alien_bullet_group.add(alien_bullet)
                settings.last_alien_shot = settings.time_now

         
             if len(alien_group)==0:
               settings.game_over=1
      
             if settings.game_over == 0 :
                 
                if len(spaceship_group) > 0: 
                    settings.game_over =  spaceship.update() 

                bullet_group.update()
                alien_group.update()
                alien_bullet_group.update()
    
             else:
                  if settings.game_over == -1:
                      draw_text('GAME OVER!', settings.font40, settings.white, 
                            int(settings.screen_width/2 - 100),
                            int(settings.screen_height/2 + 50))
                
                  if settings.game_over == 1 :
                          draw_text('YOU WIN', settings.font40, settings.white, 
                            int(settings.screen_width/2 - 100),
                            int(settings.screen_height/2 + 50))

    
          

        if settings.countdown> 0:

             draw_text('GET READY!!!', settings.font40,settings.white,
                  int(settings.screen_width/2 - 110), 
                  int(settings.screen_height/2 + 50))
          
             draw_text(str(settings.countdown), settings.font40, settings.white,
                   int(settings.screen_width/2 - 10),
                     int(settings.screen_height/2 + 100))
        
             count_timer = pygame.time.get_ticks()

             if count_timer - settings.last_count > 1000:
                  settings.countdown -= 1
                  settings.last_count= count_timer
    
    
    
        explosion_group.update()




        spaceship_group.draw(settings.screen)
        bullet_group.draw(settings.screen)
        alien_group.draw(settings.screen)
        alien_bullet_group.draw(settings.screen)
        explosion_group.draw(settings.screen)


        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                 run=False


        pygame.display.update()

    pygame.quit() 