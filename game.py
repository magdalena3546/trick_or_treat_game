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
        self.food_timer = 0
        self.score = 0
        self.poison_timer_rate = 0
        self.poison_chance = 0.3
        self.create_food()

    def show_score(self):
        font = pg.font.Font(None, 36)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

    def create_food(self):
        for _ in range(5):
            x = random.randint(0, 550)
            if random.random() < self.poison_chance:
                food_type = 'poison'
            else:
                food_type = 'candy'

            elm = Food(x, 10, food_type=food_type)
            self.food_sprites.add(elm)
            self.all_sprites.add(elm)


    def draw(self):
        self.screen.blit(self.image, (0, 0))
        self.all_sprites.draw(self.screen)
        self.show_score()
        pg.display.flip()
        

    def update(self):
        self.all_sprites.update()
        self.food_sprites.update()

    def check_collisions(self):
        collisions = pg.sprite.spritecollide(self.monster, self.food_sprites, True)
        for elm in collisions:
            if elm.rect.bottom >= self.monster.rect.top:
                if elm.food_type == 'candy':
                    self.score += 5
                else: 
                    self.score -= 5

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
            self.poison_timer_rate += 1 
            if self.poison_timer_rate >= 500:
                self.poison_chance = min(self.poison_chance + 0.05, 0.5)
                self.poison_timer_rate = 0

            self.check_collisions()
            self.draw()
            self.clock.tick(30)




