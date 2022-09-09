from pygame.sprite import Sprite
from utils.constants import SCREEN_HEIGHT
import random 


class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(900, 1100) 
        self.rect.y = random.randint(250, 300) 
        self.start_time = 0
        self.width = self.image.get_width()
        self.type = type


    def update(self, game_speed, powerups):
        self.rect.x -= game_speed

        if self.rect.x < -self.width:
            powerups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        


