import pygame as pg
import pygame.sprite 
import random 

class Food(pg.sprite.Sprite):
    def __init__(self, x, y, food_type = 'candy'):
        super().__init__()
        self.velocity = random.randint(1, 5)
        self.food_type = food_type
        if food_type == 'candy':
            self.image = pg.image.load("images/candy.png").convert_alpha()
        elif food_type == 'poison':
            self.image = pg.image.load("images/poison.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def move(self):
        self.rect.y += self.velocity
        
    def update(self):
        self.move()
        if self.rect.top > 400:
            self.kill()


        