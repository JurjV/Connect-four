import pygame
import random


class Console:
    def __init__(self, service, screen):
        self.screen = screen
        self.service = service
        self.moves = 0

    def ui_verify_winner(self):
        self.screen.winner = self.service.verify_winner()
        if self.screen.winner == "Blue":
            self.screen.colour = 'Blue'
        elif self.screen.winner == "Red":
            self.screen.colour = 'Red'

    def ui_change_matrix_value(self, event, player):
        ok = False
        if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6,
                         pygame.K_7]:
            key = event.key
            ok = self.service.check_validity(key)
            if ok:
                self.service.change_matrix_data(key, player)
                self.ui_verify_winner()
                self.moves += 1
        return ok

    def ui_computer_move(self):
        choice = self.service.computer_move_options()
        if choice == -1:
            while True:
                choice = random.randint(49, 55)
                ok = self.service.check_validity(choice)
                if ok:
                    break
        self.service.change_matrix_data(choice, 'PC')
        self.moves += 1

    def run_console_graphical(self):
        ok1 = 0
        while True:
            exit_button = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit_button = True
                    break
                if event.type == pygame.KEYDOWN and ok1 == 1 and self.screen.winner is None:
                    ok2 = self.ui_change_matrix_value(event, 'User')
                    if self.moves == 42:
                        ok1 = 2
                        self.moves += 1
                    if ok2 and ok1 != 2:
                        self.ui_computer_move()
                        self.ui_verify_winner()
                        if self.moves == 42:
                            ok1 = 2
                            self.moves += 1
                elif self.screen.winner is not None:
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                        self.service.reset_table()
                        ok1 = 1
                        self.moves = 0
                        self.screen.winner = None
                if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN) and (
                        ok1 != 2 and self.screen.winner is None):
                    ok1 = 1

            if exit_button:
                break
            if self.screen.winner is None:
                if ok1 == 0:
                    self.screen.screen_display.blit(self.screen.text2_surface, (260, 90))
                    self.screen.screen_display.blit(self.screen.text1_surface, (295, 300))
                elif ok1 == 1:
                    self.screen.screen_display.blit(self.screen.surface, self.screen.surface_position)
                    self.screen.generate_board(self.screen.digits_surface)
                else:
                    self.screen.winner = 'Tie'
            else:
                if self.screen.winner != 'Tie':
                    self.screen.generate_board(self.screen.digits_surface)
                    winner_text = self.screen.text_font.render(f'Winner is {str(self.screen.colour)}.', False, 'Black')
                    self.screen.screen_display.blit(winner_text, (350, 175))
                else:
                    self.screen.screen_display.generate_board(self.screen.digits_surface)
                    self.screen.screen_display.blit(self.screen.game_over_text, (310, 175))
                self.screen.screen_display.blit(self.screen.restart_text, (260, 300))
            pygame.display.update()
            self.screen.clock.tick(60)

    def ui_display_console_board(self):
        ok, aux_board = self.service.display_console_board()
        if ok == 0:
            print("There seems to be a tie.")
            return False
        print(aux_board)
        print("  ^  ^  ^  ^  ^  ^  ^")
        print("  1  2  3  4  5  6  7  ")
        return True

    def console_verify_winner(self):
        winner = self.service.verify_winner()
        if winner is not None:
            ok, aux_board = self.service.display_console_board()
            print(aux_board)
            self.service.reset_table()
            if winner == 'Blue':
                print("You won!")
            else:
                print("The computer won!")
            return True
        return False

    def run_console(self):
        while True:
            ok = self.ui_display_console_board()
            if not ok:
                break
            print("Choose the column you want to place your circle.")
            print("Or press  \"x\" to exit.")
            opt = input(">")
            if opt == "x":
                break
            try:
                column = int(opt)
                if column not in range(1, 8) or not self.service.check_validity(column + 48):
                    print("That is not a valid column!")
                else:
                    self.service.change_matrix_data(column + 48, 'User')
                    ok = self.console_verify_winner()
                    if ok:
                        break
                    self.ui_computer_move()
                    ok = self.console_verify_winner()
                    if ok:
                        break
            except ValueError as ve:
                print(f"That is not a valid option, {ve}.")
