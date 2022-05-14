import pygame.font
from pygame.sprite import Group
from miniship import Miniship

class Scoreboard:
    """Class to report scoring info"""
    
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = str(f"Score: {'{:,}'.format(rounded_score)}")
        self.score_image = self.font.render(score_str, True,
                            self.text_color, self.settings.bg_color)
        
        #Coordinates for score
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn high score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = str(f"High Score: {'{:}'.format(high_score)}")
        self.high_score_image = self.font.render(high_score_str, True, 
                                                    self.text_color, self.settings.bg_color)

        #center at top
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """turn level into rendered image"""
        level_str = str(f"Level: {self.stats.level}")
        self.level_image = self.font.render(level_str, True, 
                                                self.text_color, self.settings.bg_color)
        
        #coordinates for score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom
    
    def prep_ships(self):
        """Show how many ship are left"""
        self.miniships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Miniship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.miniships.add(ship)

    def show_score(self):
        """Draw score, levels, and ships on screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.miniships.draw(self.screen)

    def check_high_scores(self):
        """Check if there's new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()