  
"""

Entry point of the game.

Main Menu → Player → Game Loop → repeat.


"""




from __future__ import annotations
import pygame
import settings
from game import rungame, run_menu, show_instructions, save_score

if __name__ == "__main__":
    while True:
         
        if not run_menu():
          break

        if not show_instructions():
           break


        while rungame():
              pass

    if settings.player_name:
      save_score(settings.player_name, settings.score)

    
    pygame.quit()
    
