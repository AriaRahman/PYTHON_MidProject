from __future__ import annotations
import pygame
import settings



game_background=pygame.image.load("images/space.jpg")




def load_clean_image(path: str , remove_white: bool = True) -> pygame.Surface:
    img = pygame.image.load(path).convert_alpha()
    if remove_white:
        width, height = img.get_size()
        for x1 in range(width):
            for y1 in range(height):
                r, g, b, a = img.get_at((x1, y1))
                if r > 200 and g > 200 and b > 200:
                    img.set_at((x1, y1), (0, 0, 0, 0))
    return img



bullet_img = pygame.transform.scale(
    load_clean_image("images/bullet.png"), (40, 40))
spaceship_img = pygame.transform.scale(
    load_clean_image("images/spaceship.png"), (150, 70))
invader_bullet= pygame.transform.scale(
    load_clean_image("images/invaderbullet.png"), (20,20))



def draw_bg() -> None:
    settings.screen.blit(game_background,(0,0))

def draw_text(text : str , font: pygame.font.Font, text_col: tuple , x : int , y: int ) -> None:

    img = font.render(text, True, text_col)
    settings.screen.blit(img, (x,y))