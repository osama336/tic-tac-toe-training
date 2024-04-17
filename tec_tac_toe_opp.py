
class TicTacToe:
    def __init__(self, player=str, computer=str, is_first=bool):
        self.__board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.__player = player
        self.__computer = computer
        self.__startFirst = is_first

    def __get_board(self):
        return self.__board.copy()

    board = property(
        fget=__get_board
    )

    def __get_player(self):
        return self.__player

    player = property(
        fget=__get_player
    )

    def __get_computer(self):
        return self.__computer

    computer = property(
        fget=__get_computer
    )

    def __get_is_first(self):
        return self.__startFirst

    is_first = property(
        fget=__get_is_first
    )

    def _select_player_char(self):
        while True:
            plr = input("X or O? ").upper()
            if plr == "X":
                self.__player = "X"
                self.__computer = "O"
                break
            elif plr == "O":
                self.__player = "O"
                self.__computer = "X"
                break
            else:
                print("Try again. Please enter a valid option.")

    def _is_first(self):
        while True:
            inp = input("Do you want to start first [Y/N]? ").upper()
            if inp in ["Y", "YES", "OKAY"]:
                return True
            elif inp in ["N", "NO", "NOT SURE"]:
                return False
            else:
                print("Try again. Please enter a valid option [Y or N].")

    def _build_board(self):
        print('-' * 40)
        for row in self.__board:
            print(f'|\t{row[0]}\t|\t{row[1]}\t|\t{row[2]}\t|')
            print('-' * 40)

    def _list_of_empty_locations(self):
        lst = []
        for row in self.__board:
            for col in row:
                if isinstance(col, int):
                    lst.append(col)
        return lst

    def _location_position_mapping(self, location):
        row = (location - 1) // 3
        col = (location - 1) % 3
        return row, col

    def _is_board_full(self, board):
        return all(isinstance(cell, str) for row in board for cell in row)

    def _computer_move(self):
        best_score = -float('inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if isinstance(self.__board[row][col], int):
                    self.__board[row][col] = self.__computer
                    score = self._minimax(self.__board, 0, False)
                    self.__board[row][col] = row * 3 + col + 1
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
                    self.__board[row][col] = row * 3 + col + 1
        row, col = best_move
        self.__board[row][col] = self.__computer

    def _minimax(self, board, depth, is_maximizing):
        if self._check_winner(board, self.__player):
            return -10 + depth
        elif self._check_winner(board, self.__computer):
            return 10 - depth
        elif self._is_board_full(board):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if isinstance(board[row][col], int):
                        board[row][col] = self.__computer
                        score = self._minimax(board, depth + 1, False)
                        board[row][col] = row * 3 + col + 1
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if isinstance(board[row][col], int):
                        board[row][col] = self.__player
                        score = self._minimax(board, depth + 1, True)
                        board[row][col] = row * 3 + col + 1
                        best_score = min(score, best_score)
            return best_score

    def _check_winner(self, board, player):
        for i in range(3):
            if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
                return True

        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def _player_move(self):
        free = self._list_of_empty_locations()
        while True:
            try:
                location = int(input(f"Enter the location of your move\nAvailable location {free}: "))
            except ValueError:
                print("Please make sure to enter an integer location.")
                continue

            if location not in free:
                print(f"Please make sure to use an empty location {free}.")
                continue
            else:
                break

        row, col = self._location_position_mapping(location)
        self.__board[row][col] = self.__player

    def play_game(self):
        self._select_player_char()
        print(f"You will be playing with {self.__player}, Computer will play with {self.__computer}")

        first = self._is_first()
        print(f"You chose to play {'First' if first else 'second'}")

        self._build_board()
        while True:
            if first:
                self._player_move()
                self._build_board()
                if self._check_winner(self.__board, self.__player):
                    print(f"{self.__player} wins!")
                    break
                if len(self._list_of_empty_locations()) == 0 or self._check_winner(self.__board, self.__computer):
                    print("It's a tie!")
                    break
                self._computer_move()
                self._build_board()
                if self._check_winner(self.__board, self.__computer):
                    print(f"{self.__computer} wins!")
                    break
                if len(self._list_of_empty_locations()) == 0 or self._check_winner(self.__board, self.__computer):
                    print("It's a tie!")
                    break
            else:
                self._computer_move()
                self._build_board()
                if self._check_winner(self.__board, self.__computer):
                    print(f"{self.__computer} wins!")
                    break
                if len(self._list_of_empty_locations()) == 0 or self._check_winner(self.__board, self.__player):
                    print("It's a tie!")
                    break
                self._player_move()
                self._build_board()
                if self._check_winner(self.__board, self.__player):
                    print(f"{self.__player} wins!")
                    break
                if len(self._list_of_empty_locations()) == 0 or self._check_winner(self.__board, self.__player):
                    print("It's a tie!")
                    break

if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()

