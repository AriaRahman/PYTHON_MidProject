from __future__ import annotations
import pygame
from game import rungame, run_menu, show_instructions

if __name__ == "__main__":
    if run_menu():
         if show_instructions():
             rungame()
         else:
              pygame.quit()
    else:
         pygame.quit()
    
