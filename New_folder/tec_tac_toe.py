import random

class TicTacToe:
    def __init__(self):
        self._board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self._player = None
        self._computer = None

    def _select_player_char(self):
        while True:
            plr = input("X or O? ").upper()
            if plr == "X":
                self._player = "X"
                self._computer = "O"
                break
            elif plr == "O":
                self._player = "O"
                self._computer = "X"
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
        for row in self._board:
            print(f'|\t{row[0]}\t|\t{row[1]}\t|\t{row[2]}\t|')
            print('-' * 40)

    def _list_of_empty_locations(self):
        lst = []
        for row in self._board:
            for col in row:
                if isinstance(col, int):
                    lst.append(col)
        return lst

    def _location_position_mapping(self, location):
        row = (location - 1) // 3
        col = (location - 1) % 3
        return row, col

    def _computer_move(self):
        best_score = -float('inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if isinstance(self._board[row][col], int):
                    self._board[row][col] = self._computer
                    score = self._minimax(self._board, 0, False)
                    self._board[row][col] = row * 3 + col + 1  # Incorrect
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
                    self._board[row][col] = row * 3 + col + 1  # Incorrect
        row, col = best_move
        self._board[row][col] = self._computer

    def _minimax(self, board, depth, is_maximizing):
        if self._check_winner(board, self._player):
            return -10 + depth
        elif self._check_winner(board, self._computer):
            return 10 - depth
        elif self._is_board_full(board):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if isinstance(board[row][col], int):
                        board[row][col] = self._computer
                        score = self._minimax(board, depth + 1, False)
                        board[row][col] = row * 3 + col + 1
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if isinstance(board[row][col], int):
                        board[row][col] = self._player
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

    def _is_board_full(self, board):
        return all(isinstance(cell, str) for row in board for cell in row)

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
        self._board[row][col] = self._player

    def play_game(self):
        self._select_player_char()
        print(f"You will be playing with {self._player}, Computer will play with {self._computer}")

        first = self._is_first()
        print(f"You chose to play {'First' if first else 'second'}")

        self._build_board()
        while True:
            if first:
                self._player_move()
                self._build_board()
                if self._check_winner(self._board, self._player):
                    print(f"{self._player} wins!")
                    break
                if self._is_board_full(self._board):
                    print("It's a tie!")
                    break
                self._computer_move()
                self._build_board()
                if self._check_winner(self._board, self._computer):
                    print(f"{self._computer} wins!")
                    break
                if self._is_board_full(self._board):
                    print("It's a tie!")
                    break
            else:
                self._computer_move()
                self._build_board()
                if self._check_winner(self._board, self._computer):
                    print(f"{self._computer} wins!")
                    break
                if self._is_board_full(self._board):
                    print("It's a tie!")
                    break
                self._player_move()
                self._build_board()
                if self._check_winner(self._board, self._player):
                    print(f"{self._player} wins!")
                    break
                if self._is_board_full(self._board):
                    print("It's a tie!")
                    break

if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()





