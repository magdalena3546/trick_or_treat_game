import pygame as pg
import pygame.sprite 
import random 

class Food(pg.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pg.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = random.randint(1, 5)
    
    def move(self):
        self.rect.y += self.velocity
        
    def update(self):
        self.move()
        if self.rect.top > 400:
            self.kill()


        