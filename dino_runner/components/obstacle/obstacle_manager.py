import pygame 
from components.obstacle.cactus import (
    SmallCactus,
    LargeCactus,
    Bird_high,
    Bird_low,
)
import random 
from components.dinosaur import Dinosaur 
from utils.constants import SMALL_CACTUS
from utils.constants import LARGE_CACTUS
from utils.constants import BIRD, DEFAULT_TYPE
class ObstacleManager():
    def __init__(self):
        #self.obstacles = []
        self.obstacles = []
        self.dinosaur = Dinosaur

    def update(self, game):
        self.random_number = random.randint(0,3)
        if len(self.obstacles) == 0:
            if self.random_number == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            if self.random_number == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            if self.random_number == 2:
               self.obstacles.append(Bird_low(BIRD))
            if self.random_number == 3:
                self.obstacles.append(Bird_high(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.dinosaur.dino_rect.colliderect(obstacle.rect):
                if not game.dinosaur_shield:
                    pygame.time.delay(300)
                    game.playing = False
                else:
                    self.obstacles.remove(obstacle)
                    game.dinosaur_shield = False 
                    game.dinosaur.type = DEFAULT_TYPE ##Cambio para que solo funcione una vez, aun así tiene un tiempo limite 


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
        
