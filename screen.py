import pygame


class Screen:
    def __init__(self, service):
        self.service = service
        pygame.init()
        self.size = (960, 770)
        self.screen_display = pygame.display.set_mode(self.size)
        self.text_font = pygame.font.Font(None, 50)
        self.winner = None
        self.colour = 'White'
        pygame.display.set_caption("\"Connect four\" by Jurj Victor")
        self.clock = pygame.time.Clock()
        self.surface = pygame.Surface(self.size)
        self.surface_position = (0, 0)
        self.surface.fill('Orange2')
        self.text1_surface = self.text_font.render('Press any key to begin', False, 'white')
        self.text2_surface = self.text_font.render('Welcome to \"Connect four!\"', False, 'white')
        self.digits_surface = self.ui_prepare_nr_format(self.text_font)
        self.game_over_text = self.text_font.render('Game over!', False, 'Black')
        self.restart_text = self.text_font.render('Press any button to restart.', False, 'Black')

    def generate_board(self, digits_surface):
        """
        This is the function that changes the board depending on the moves made by
        the computer and the user.
        :param digits_surface: the digits to be placed at the bottom of the screen
        """
        dist = 0
        for x in range(1, 8):
            for y in range(0, 6):
                colour = self.service.choose_colour(x - 1, y)
                pygame.draw.circle(self.screen_display, colour, (120 * x, 65 + 120 * y), 50, 0)
                pygame.draw.circle(self.screen_display, 'black', (120 * x, 65 + 120 * y), 50, 2)
            y = 6
            self.screen_display.blit(digits_surface[x - 1], (dist + 110 * x, 10 + 120 * y))
            dist += 10

    def ui_prepare_nr_format(self, text_font):
        return self.service.prepare_numbers_format(text_font)

