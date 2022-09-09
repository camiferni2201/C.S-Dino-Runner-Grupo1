import pygame
from utils import text_utils
from components.obstacle.obstacle_manager import ObstacleManager
from utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, RESET, GAME_OVER
from components.dinosaur import Dinosaur 
from components.powerups.power_up_manager import PowerUpManager
import random


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 14
        self.x_pos_cloud = SCREEN_WIDTH
        self.y_pos_cloud = random.randint(100, 125)
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.y_pos_reset = (SCREEN_HEIGHT // 2) - 35
        self.x_pos_reset = (SCREEN_WIDTH // 2) -35
        self.x_pos_reset_gameover = (SCREEN_WIDTH // 2) -190
        self.y_pos_reset_gameover = (SCREEN_HEIGHT // 2) - 150
        self.dinosaur = Dinosaur() ##Atributo para poder usar en los otros contextos
        self.obstacle_manager = ObstacleManager()
        self.points= 0
        self.game_running = True 
        self.first_game_running = True 
        self.index_show_menu = 1
        self.game_over = True 
        self.index_high_score = 1
        self.power_up_manager = PowerUpManager()
        self.dinosaur_shield = False
        #self.sound_dead = pygame.mixer.Sound('DinoDie.mpeg')

    def run(self):
        # Game loop: events - update - draw
        self.reset_components()
        self.dinosaur_shield = False 
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_components(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.points = 0
        self.game_speed = 14

    def execute(self):
        while self.game_running:
            if self.index_show_menu == 2:
                if not self.playing:
                    self.show_menu_reset()
                    self.index_high_score = 2
                    
            
            elif self.index_show_menu == 1:
                if not self.playing:
                    self.show_menu()
                    

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.game_running = False
                

    def update(self):
        user_input = pygame.key.get_pressed()
        self.dinosaur.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)


    def draw(self):
        
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_background_clouds()
        self.dinosaur.draw(self.screen)
        self.show_score()
        self.highest_score()
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_background_clouds(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud= SCREEN_WIDTH
        self.x_pos_cloud -= self.game_speed

    def draw_menu_reset(self):
            self.screen.blit(RESET,  (self.x_pos_reset, self.y_pos_reset))
            self.screen.blit(GAME_OVER,  (self.x_pos_reset_gameover, self.y_pos_reset_gameover))
           

    def show_menu_reset(self):
        self.game_running = True 
       
        self.draw_menu_reset()
        pygame.display.update()
        self.handle_key_events_menu()

    def show_score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        text, text_rect = text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)

    def highest_score(self):
        if self.index_high_score == 1:
            self.high_score = 0
            text, text_rect = text_utils.get_high_score_element(self.high_score)
            self.screen.blit(text,text_rect)
            
        if self.index_high_score == 2:   
            if self.high_score > self.points:
                text, text_rect = text_utils.get_high_score_element(self.high_score)
                self.screen.blit(text,text_rect)
            elif self.high_score <= self.points:
                text, text_rect = text_utils.get_high_score_element(self.points)
                self.screen.blit(text,text_rect)

    def show_menu(self):
        self.game_running = True

        white_color = (255, 255, 255)
        self.screen.fill(white_color)

        self.show_options_menu()

        pygame.display.update()

        self.handle_key_events_menu()

    def show_options_menu(self):
        half_screen_heigth = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        text, text_rect = text_utils.get_text_element('Press any key to Start', half_screen_width, half_screen_heigth)

        self.screen.blit(text, text_rect)

    def handle_key_events_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.game_running = False
                #self.sound_dead.play()
                
                
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                self.run()
                self.index_show_menu = 2

            