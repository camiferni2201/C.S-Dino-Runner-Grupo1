import pygame 
from components.cactus import (
    SmallCactus,
    LargeCactus,
    Bird
)
from random import choice
number_list = [
    0,
    1,
    2,
]
from utils.constants import SMALL_CACTUS
from utils.constants import LARGE_CACTUS
from utils.constants import BIRD
class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if choice(number_list) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            if choice(number_list) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            if choice(number_list) == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.dinosaur.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(300)
                game.playing = False


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            