from __future__ import annotations

import random
import os
import csv
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

PLAYER_FILE = "Players.csv"

cx = settings.screen_width  // 2
cy = settings.screen_height // 2


def loadplayers() -> list[str]:
     if not os.path.exists(PLAYER_FILE):
          return[]
     with open(PLAYER_FILE,'r', newline="") as f:
          reader = csv.DictReader(f)
          return [{"name": row["name"], "score": int(row["score"])} for row in reader]

def saveplayers(players: list[dict]) -> None:
     with open(PLAYER_FILE, 'w', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(players)


def getplayer() -> list[str]:
    return [p["name"].lower() for p in loadplayers()]
 
 

def save_score(name: str, score: int) -> None:
    players = loadplayers()
    for p in players:
        if p["name"].lower() == name.lower():
            p["score"] = score
            saveplayers(players)
            return

def validate_save(name_text: str) -> str:
    name = name_text.strip()

    if len(name) == 0:
        return "Name cannot be empty!"
    
    if len(name) < 2:
        return "Name must be at least 2 characters!"
    
    if not name.replace(" ", "").isalpha():

        return "Letters only please!"
    
    if name.lower() in getplayer():

        return "Name already taken!"
    


    players = loadplayers()
    players.append({"name": name, "score": 0})
    saveplayers(players)
    settings.player_name = name
    return ""


def run_menu() -> bool:


    btn_start  = MenuButton(cx, cy,300, 50, "START GAME", enabled=True)
    btn_scores = MenuButton(cx, cy + 80, 300, 50, "HIGH SCORES",enabled=False)
 
    buttons = [btn_start, btn_scores]
 
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

    input_box = pygame.Rect(0,0,360,50)
    input_box.center=(cx,cy-80)

    enter_btn = MenuButton(cx, cy, 200, 45, "ENTER", enabled=True,color= settings.enter_color)

    name_txt=""
    error_txt=""

    while True:
        settings.clock.tick(settings.fps)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
     
            if event.type == pygame.KEYDOWN:
                 
                if event.key == pygame.K_BACKSPACE:
                    name_txt = name_txt[:-1]
                    error_txt = ""
                elif event.key == pygame.K_RETURN:
                    error_txt = validate_save (name_txt)

                    if error_txt == "":
                        return True
                    
                elif len(name_txt) < 16:
                    if event.unicode.isprintable() and event.unicode != " ":
                        name_txt += event.unicode
                        error_txt = ""
 
            if enter_btn.handle_event(event):
                error_txt = validate_save(name_txt)
                if error_txt == "":
                    return True
 
        draw_bg()

        label = settings.font30.render("PLAYER NAME", True, settings.white)
        settings.screen.blit(label, label.get_rect(centerx=cx, centery=cy - 140))
       
       
        pygame.draw.rect(settings.screen, settings.white, input_box)
        pygame.draw.rect(settings.screen, (0, 0, 0), input_box, 2)
        name_surf = settings.font30.render(name_txt, True, (0, 0, 0))
        settings.screen.blit(name_surf, name_surf.get_rect(center=input_box.center))

        enter_btn.draw(settings.screen)

        if error_txt:
             err = settings.font30.render(error_txt,True, settings.errcolor)
             settings.screen.blit(err,err.get_rect(centerx = cx , centery = cy +55))

        
        pygame.draw.line(settings.screen, settings.white,
                         (cx - 250, cy + 80), (cx + 250, cy + 80), 1)


        lines= [
            (settings.font40, 'HOW TO PLAY',cy + 120),
            (settings.font30, 'USE < > TO MOVE LEFT/RIGHT', cy + 190),
            (settings.font30, 'USE SPACE TO SHOOT', cy+240),]

        for font, text , y in lines:
            rules= font.render(text, True, settings.white)
            settings.screen.blit(rules,(cx - rules.get_width()//2,y))

        pygame.display.update()

 




def rungame() -> None:
    create_aliens()
    spaceship= create_spaceship()

    settings.game_over = 0
    settings.countdown = 3
    settings.score=0
    settings.last_count = pygame.time.get_ticks()
    settings.last_alien_shot = pygame.time.get_ticks()


    quit_btn = MenuButton(settings.screen_width - 70 , 30 , 110, 40,
                          "QUIT", enabled= True, color = settings.quit_color)
    

    restart_btn = MenuButton(int(settings.screen_width / 2), 
                             int(settings.screen_height / 2 + 120),
                             200, 50, "RESTART", enabled=True)
    



    def clear_save():
        if settings.player_name:
            save_score(settings.player_name, settings.score)  
        spaceship_group.empty()
        bullet_group.empty()
        alien_group.empty()
        alien_bullet_group.empty()
        explosion_group.empty()
    
    run= True

    while run:
        settings.clock.tick(settings.fps)
        settings.time_now = pygame.time.get_ticks()

        draw_bg()
  
        if settings.countdown == 0 : 

   
             if settings.time_now - settings.last_alien_shot > settings.alien_cooldown and len(alien_bullet_group) < 15 and len(alien_group) > 0 :
        
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
                  
                  restart_btn.draw(settings.screen) 

    
          

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
        

        draw_text(f'Score: {settings.score}', settings.font30, settings.white, 10, 10)

        quit_btn.draw(settings.screen)


        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                 return False
            
           if quit_btn.handle_event(event):
                clear_save()
                spaceship_group.empty()
                bullet_group.empty()
                alien_group.empty()
                alien_bullet_group.empty()
                explosion_group.empty()
                return False
           
           if settings.game_over != 0 and restart_btn.handle_event(event):
                

                clear_save()
                spaceship_group.empty()
                bullet_group.empty()
                alien_group.empty()
                alien_bullet_group.empty()
                explosion_group.empty()
                return True   
           

        pygame.display.update()

    return False