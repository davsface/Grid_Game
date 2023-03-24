# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class GameBoard:

    def __init__(self, board_size):
        self.board_size = board_size
        self.char_loc = [None] * 2
        self.goal_loc = [None] * 2
        self.move_count = 0
        self.game_board = [['o' for row in range(self.board_size)] for column in range(self.board_size)]

    def print_game_board(self):
        print('\n')
        for row in self.game_board:
            print(row)
        print('\n')

    def place_character(self, row_loc, col_loc):
        """
        place_character places a character token on the game board

        :param row_loc: x coordinate of the character
        :param col_loc: y coordinate of the character

        :return: None
        """

        if type(row_loc) != int or type(col_loc) != int:
            print("ERROR: Please enter a valid coordinate")
        elif row_loc < 0 or col_loc < 0 or row_loc > (self.board_size-1) or col_loc > (self.board_size-1):
            print("ERROR: Please enter a valid coordinate")

        self.game_board[row_loc][col_loc] = 'c'
        self.char_loc = [row_loc, col_loc]
        self.check_goal()

    def place_goal(self, row_loc, col_loc):
        """
        place_goal places a goal token on the game board

        :param row_loc: x coordinate of the character
        :param col_loc: y coordinate of the character

        :return: None
        """

        if type(row_loc) != int or type(col_loc) != int:
            print("ERROR: Please enter a valid coordinate")
        elif row_loc < 0 or col_loc < 0 or row_loc > (self.board_size-1) or col_loc > (self.board_size-1):
            print("ERROR: Please enter a valid coordinate")

        self.game_board[row_loc][col_loc] = 'g'
        self.goal_loc = [row_loc, col_loc]
        self.check_goal()

    def check_goal(self):
        """
        check_goal checks to see if the character token has reached the goal token

        :return: None
        """
        if self.check_placed() == 0:
            return

        if self.char_loc[0] == self.goal_loc[0] and self.char_loc[1] == self.goal_loc[1]:
            print("Congratulations! You've reached the goal and it only took x moves")

    def check_placed(self):
        if self.goal_loc[0] is None or self.goal_loc[1] is None:
            return 0
        elif self.char_loc[0] is None or self.char_loc[1] is None:
            return 0

        return 1

    def move_left(self):
        """
        move_left moves the character token one space to the left on the game board if the move is valid and checks
        if the goal has been reached. Each valid call increments self.move_count and update self.char_loc

        :return: None
        """

        if self.check_placed() == 0:
            print("Character or goal has not yet been placed")
            return

        elif (self.char_loc[1]-1) < 0:
            print("Invalid move, please pick another path")
            return
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'o'
        self.char_loc[1] = self.char_loc[1] - 1
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'c'
        self.move_count += 1

    def move_right(self):
        """
        move_right moves the character token one space to the right on the game board if the move is valid and checks
        if the goal has been reached. Each valid call increments self.move_count and update self.char_loc

        :return: None
        """

        if self.check_placed() == 0:
            print("Character or goal has not yet been placed")
            return

        elif (self.char_loc[1]+1) >= self.board_size:
            print("Invalid move, please pick another path")
            return
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'o'
        self.char_loc[1] = self.char_loc[1] + 1
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'c'
        self.move_count += 1

    def move_up(self):
        """
        move_up moves the character token one space to the up on the game board if the move is valid and checks
        if the goal has been reached. Each valid call increments self.move_count and update self.char_loc

        :return: None
        """

        if self.check_placed() == 0:
            print("Character or goal has not yet been placed")
            return

        elif (self.char_loc[0]-1) < 0:
            print("Invalid move, please pick another path")
            return
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'o'
        self.char_loc[1] = self.char_loc[0] - 1
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'c'
        self.move_count += 1

    def move_down(self):
        """
        move_down moves the character token one space to the down on the game board if the move is valid and checks
        if the goal has been reached. Each valid call increments self.move_count and update self.char_loc

        :return: None
        """

        if self.check_placed() == 0:
            print("Character or goal has not yet been placed")
            return

        elif (self.char_loc[0]+1) >= self.board_size:
            print("Invalid move, please pick another path")
            return
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'o'
        self.char_loc[1] = self.char_loc[0] + 1
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'c'
        self.move_count += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    new_game = GameBoard(5)
    new_game.place_character(0,4)
    new_game.place_goal(0,0)
    new_game.print_game_board()
    new_game.move_left()
    new_game.move_right()
    new_game.move_right()
    new_game.print_game_board()

