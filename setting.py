import pygame 
from pygame.locals import *


clock = pygame.time.Clock()
fps=60


screen_width = 1000
screen_height= 700
screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SPACE SHOOTER")

game_background=pygame.image.load("images/space.jpg")


def draw_bg():
    screen.blit(game_background,(0,0))



class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        img = pygame.image.load("images/spaceship.png").convert_alpha()
        
        width, height = img.get_size()
        for x1 in range(width):
            for y1 in range(height):
                r, g, b, a = img.get_at((x1, y1))
               
                if r > 200 and g > 200 and b > 200:
                    img.set_at((x1, y1), (0, 0, 0, 0))  
        
        self.image = pygame.transform.scale(img, (450, 120))
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

# class Spaceship(pygame.sprite.Sprite):
#     def __init__(self,x,y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load("images/spaceship.png")
#         self.rect = self.image.get_rect()
#         self.rect.center = [x,y]

spaceship_group = pygame.sprite.Group()

spaceship= Spaceship(int(screen_width / 2),screen_height - 100)
spaceship_group.add(spaceship)



run=True
while run:
    clock.tick(fps)
    draw_bg()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    spaceship_group.draw(screen)

    pygame.display.update()
pygame.quit()