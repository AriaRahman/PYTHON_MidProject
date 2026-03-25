from __future__ import annotations
import pygame
import settings





def load_clean_image(path: str , remove_white: bool = True) -> pygame.Surface:
    img = pygame.image.load(path)
    img = img.convert_alpha() if pygame.display.get_surface() else img
    if remove_white:
        width, height = img.get_size()
        for x1 in range(width):
            for y1 in range(height):
                r, g, b, a = img.get_at((x1, y1))
                if r > 200 and g > 200 and b > 200:
                    img.set_at((x1, y1), (0, 0, 0, 0))
    return img






def draw_bg() -> None:
    settings.screen.blit(settings.game_background,(0,0))

def draw_text(text : str , font: pygame.font.Font, text_col: tuple , x : int , y: int ) -> None:

    img = font.render(text, True, text_col)
    settings.screen.blit(img, (x,y))


