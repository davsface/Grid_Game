# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class GameBoard:

    def __init__(self, board_size):
        self.game_board = [["o"] * board_size] * board_size

    def print_game_board(self):
        for y in self.game_board:
            print(y)

    def place_character(self):
        pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    new_game = GameBoard(5)
    new_game.print_game_board()

