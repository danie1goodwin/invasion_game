import pygame.font

class NameInput:

    def __init__(self, ai_game, msg):
        """Initialize Name Input attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the name_input.
        self.width, self.height = 400, 50
        self.name_input_color_inactive = (220, 220, 220)
        self.name_input_color_active = (0, 255, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 30)

        # Build the name_input's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y = 325

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        '''Turn mesg into a rendered image and puts text on the image.'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.name_input_color_inactive)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.x = self.rect.x

    def draw_name_input(self):
        # Draw blank rect and then draw message.
        self.screen.fill(self.name_input_color_inactive, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
