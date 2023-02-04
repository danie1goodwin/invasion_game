import pygame.font

class Leaderboard:

    def __init__(self, ai_game, msg):
        """Initialize Leaderboard attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the leaderboard.
        self.width, self.height = 200, 300
        self.leaderboard_color = (220, 220, 220)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 30)

        # Build the leaderboard's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y = 375

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        '''Turn msg into a rendered image and places text on the image.'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.leaderboard_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.y = self.rect.y

    def draw_leaderboard(self):
        # Draw blank leaderboard and then draw message.
        self.screen.fill(self.leaderboard_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
