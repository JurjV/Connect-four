import numpy as np
import copy


class Service:
    def __init__(self, repo):
        self.repo = repo

    @staticmethod
    def prepare_numbers_format(text_font):
        """
        This function prepares the list of digits to be printed on the
        scree using the given font.
        :return: digits_surface-the list with the digits in the given font
        """
        digits = ['1', '2', '3', '4', '5', '6', '7']
        digits_surface = []
        for i in digits:
            aux = text_font.render(i, False, 'black')
            digits_surface.append(aux)
        return digits_surface

    def check_validity(self, key):
        """
        It checks if the column is valid to place a number in it.
        :param key: column number
        :return: true/false
        """
        key = int(key) - 49
        if self.repo.matrix[0][key] != 0:
            return False
        return True

    def change_matrix_data(self, y, player):
        """
        This function takes as input the column number and changes the
        circle on the correct line to the value of the given player.
        :param y: column
        :param player: user or computer
        :return:
        """
        y = int(y) - 49
        for i in range(5, -1, -1):
            if self.repo.matrix[i][y] == 0:
                if player == 'User':
                    self.repo.matrix[i][y] = 1
                    break
                else:
                    self.repo.matrix[i][y] = 2
                    break
        # print(self.repo.matrix)

    def choose_colour(self, x, y):
        """
        This is the function that chooses the specific color for the
        bubble at index x,y in the matrix
        :param x: line
        :param y: column
        :return: color
        """
        if self.repo.matrix[y][x] == 0:
            colour = 'Grey55'
        elif self.repo.matrix[y][x] == 1:
            colour = 'Blue'
        else:
            colour = 'Red'
        return colour

    def verify_winner(self):
        """
        This function checks if the game has been won by the
        player or the computer.
        :return: the color of the winner
        """
        for i in range(0, 6):
            for j in range(0, 7):
                if self.repo.matrix[i][j] != 0:
                    winner = self.verify_all_cases(i, j)
                    if winner == 1:
                        return 'Blue'
                    if winner == 2:
                        return 'Red'
        return None

    def verify_all_cases(self, x, y):
        """
        This function checks for the position x,y in the matrix all the directions
        if there are 4 colors connected.
        :param x: line
        :param y: column
        :return: color of the winner
        """
        circles = 1
        colour = copy.deepcopy(self.repo.matrix[x][y])
        while x < 5:
            if self.repo.matrix[x + 1][y] == colour:
                circles += 1
                x += 1
            else:
                break
        if circles >= 4:
            return colour

        circles = 1
        while x > 0:
            if self.repo.matrix[x - 1][y] == colour:
                circles += 1
                x -= 1
            else:
                break
        if circles >= 4:
            return colour

        circles = 1
        while y < 6:
            if self.repo.matrix[x][y + 1] == colour:
                circles += 1
                y += 1
            else:
                break
        if circles >= 4:
            return colour

        circles = 1
        while y > 0:
            if self.repo.matrix[x][y - 1] == colour:
                circles += 1
                y -= 1
            else:
                break
        if circles >= 4:
            return colour

        circles = 1
        while x < 5 and y < 6:
            if self.repo.matrix[x + 1][y + 1] == colour:
                circles += 1
                y += 1
                x += 1
            else:
                break
        if circles >= 4:
            return colour

        circles = 1
        while x > 0 and y > 0:
            if self.repo.matrix[x - 1][y - 1] == colour:
                circles += 1
                y -= 1
                x -= 1
            else:
                break
        if circles >= 4:
            return colour

        circles = 1
        while x < 5 and y > 0:
            if self.repo.matrix[x + 1][y - 1] == colour:
                circles += 1
                x += 1
                y -= 1
            else:
                break
        if circles >= 4:
            return colour

        circles = 1
        while x > 0 and y < 6:
            if self.repo.matrix[x - 1][y + 1] == colour:
                circles += 1
                y += 1
                x -= 1
            else:
                break
        if circles >= 4:
            return colour

        return 0

    def reset_table(self):
        """
        This function resets the matrix with all zeros.
        """
        self.repo.matrix = np.zeros((6, 7))

    def computer_move_options(self):
        """
        This is the function that makes the move for the computer.
        """
        aux_matrix = copy.deepcopy(self.repo.matrix)
        x = -1
        for line in range(0, 6):
            ok = self.check_validity(line + 49)
            if ok:
                self.change_matrix_data(line + 49, 'Computer')
                winner = self.verify_winner()
                self.repo.matrix = copy.deepcopy(aux_matrix)
                if winner == 'Red':
                    x = line + 49
                    break
        if x == -1:
            for line in range(0, 6):
                ok = self.check_validity(line + 49)
                if ok:
                    self.change_matrix_data(line + 49, 'User')
                    winner = self.verify_winner()
                    self.repo.matrix = copy.deepcopy(aux_matrix)
                    if winner == 'Blue':
                        x = line + 49
                        break
        return x

    def display_console_board(self):
        """
        This function returns a copy of the board so that
        it can be printed on the screen and a value to check if
        the matrix is valid.
        :return: aux_board-copy of matrix,ok-1 or 0
        """
        ok = 0
        aux_board = copy.deepcopy(self.repo.matrix)
        for i in range(0, 6):
            for j in range(0, 7):
                if self.repo.matrix[i][j] == 0:
                    aux_board[i][j] = int(0)
                    ok = 1
                if self.repo.matrix[i][j] == 1:
                    aux_board[i][j] = int(1)
                if self.repo.matrix[i][j] == 2:
                    aux_board[i][j] = int(2)
        return ok, aux_board
