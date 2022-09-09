import pygame
import random
from components.powerups.shield import (Shield, Hammer)
from utils.constants import SHIELD_TYPE, HAMMER_TYPE

class PowerUpManager():
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0
        self.time_start = 0
        self.type = 0


    def update(self, game):
        
        self.generate_power_ups()
        for power_up in self.power_ups:
            power_up.update(game.game_speed // 4, self.power_ups)
            if game.dinosaur.dino_rect.colliderect(power_up.rect):
                if self.type <= 5:   
                    #self.time_start = pygame.time.get_ticks()
                    game.dinosaur.isShieldType = True
                    game.dinosaur.type = power_up.type
                    #power_up.start_time = pygame.time.get_ticks()
                    game.dinosaur_shield = True 
                    self.power_ups.remove(power_up)
                    self.type += 6
                
                else:
                    game.dinosaur_shield = False
                    self.type = 0
                    
                

    def generate_power_ups(self):
        self.random_number = random.randint(0,1)
        if len(self.power_ups) == 0:
            if self.random_number == 0:
                self.power_ups.append(Shield())
            if self.random_number == 1:
                self.power_ups.append(Hammer())
        
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        

