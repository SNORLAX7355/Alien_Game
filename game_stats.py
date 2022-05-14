class GameStats:
    """Track stats for Alien Game"""
    
    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Initialize stats that can change"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1