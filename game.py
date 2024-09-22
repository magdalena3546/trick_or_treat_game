import pygame as pg
from monster import Monster

class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((600, 400))
        self.running = True
        self.clock = pg.time.Clock()
        self.monster = Monster("holo")
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.monster)
        self.image = pg.image.load("images/bgc.png")

    def draw(self):
        self.screen.blit(self.image, (0, 0))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def update(self):
        self.all_sprites.update()

    def check_collisions(self):
        pass

    def handle_events(self):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(30)




