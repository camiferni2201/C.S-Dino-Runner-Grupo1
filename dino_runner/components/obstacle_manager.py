from components.cactus import (
    SmallCactus,
    LargeCactus,
    Bird
)
import random 
from utils.constants import SMALL_CACTUS
from utils.constants import LARGE_CACTUS
from utils.constants import BIRD
class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self):
        if len(self.obstacles) == 0:
            if random.randint(0,2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            if random.randint(0,2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            if random.randint(0,2) == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(15, self.obstacles)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)