import random 
from components.obstacle import Obstacle
from utils.constants import (BIRD,
    DEFAULT_TYPE) 

class SmallCactus(Obstacle):
    def __init__(self, image):
        self.index = random.randint(0,2)
        super().__init__(image, self.index)
        self.rect.y = 320

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.index = random.randint(0,2)
        super().__init__(image, self.index)
        self.rect.y = 295

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        self.index = 0
        super().__init__(image, self.index)
        self.rect.y = 230
        self.fly_index = 0
        self.fly_img = {DEFAULT_TYPE: BIRD}
        self.type = DEFAULT_TYPE
        self.image = self.fly_img[self.type][0]

    def update(self):
        self.fly()
        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.fly_index // 5], self.rect)

    def fly(self):
        self.image = self.fly_img[self.type][self.fly_index // 5]
        self.fly_index += 1



        
