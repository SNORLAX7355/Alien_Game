import pygame
from pygame.sprite import Sprite

class Miniship(Sprite):
    """mini ships for the lives"""

    def __init__(self, ai_game):
        """initialize miniship"""    
        super().__init__()   
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get rect
        self.image = pygame.image.load('Alien Game\images\miniship.bmp')
        self.rect = self.image.get_rect()