  
"""

Entry point of the game.

Main Menu → Player → Game Loop → repeat.


"""




from __future__ import annotations
import pygame
from game import rungame, run_menu, show_instructions

if __name__ == "__main__":
    while True:
         
        if not run_menu():
          break

        if not show_instructions():
           break


        while rungame():
              pass
    
    pygame.quit()
    
