import pygame as pg

class Monster(pg.sprite.Sprite):
    def __init__(self, user_name):
        super().__init__()
        self.speed = 10
        self.name = user_name
        self.image = pg.image.load("images/vampire1.png").convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y =100
        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        self.move()

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] and self.rect.right<600:
            self.rect.x += self.speed
        