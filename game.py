import pygame as pg
from monster import Monster
from food import Food
import random

class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((600, 400))
        self.running = True
        self.clock = pg.time.Clock()
        self.monster = Monster("holo")
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.monster)
        self.food_sprites = pg.sprite.Group()
        self.image = pg.image.load("images/bgc.png")
        self.create_food()
        self.food_timer = 0

    def create_food(self):
        for _ in range(5):
            x = random.randint(0, 550)
            elm = Food(x, 10, image_path="images/candy.png")
            self.food_sprites.add(elm)
            self.all_sprites.add(elm)

    def draw(self):
        self.screen.blit(self.image, (0, 0))
        self.all_sprites.draw(self.screen)
        pg.display.flip()
        

    def update(self):
        self.all_sprites.update()
        self.food_sprites.update()

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

            self.food_timer += 1
            if self.food_timer >= 100:
                self.create_food()
                self.food_timer = 0

            self.draw()

            self.clock.tick(30)




