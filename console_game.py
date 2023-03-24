import random
class GameBoard:
    """
    A class representing a game board with a character and a goal. The board size is specified upon initialization.
    Methods are provided to place the character and goal on the board, move the character left or right on the board,
    print the current board configuration, and check if the character has reached the goal.

    ...

    Attributes
    ----------
    board_size : int
        The size of the square game board.
    char_loc : list
        The (row, column) location of the character on the board.
    goal_loc : list
        The (row, column) location of the goal on the board.
    move_count : int
        The number of moves the character has made.
    game_board : list
        A 2D list representing the current state of the game board.

    Methods
    -------
    print_game_board():
        Prints the current state of the game board in a readable way.
    place_character(row_loc, col_loc):
        Places the character token on the board at the specified (row, column) location.
    place_goal(row_loc, col_loc):
        Places the goal token on the board at the specified (row, column) location.
    check_goal():
        Checks if the character has reached the goal, and prints a congratulatory message if so.
    check_placed():
        Checks if both the character and goal tokens have been placed on the board.
    move_left():
        Moves the character token one space to the left on the board, if the move is valid.
    move_right():
        Moves the character token one space to the right on the board, if the move is valid.
    """

    def __init__(self, board_size):
        self.board_size = board_size
        self.char_loc = [None] * 2
        self.goal_loc = [None] * 2
        self.move_count = 0
        self.game_board = [['o' for row in range(self.board_size)] for column in range(self.board_size)]

    def print_game_board(self):
        """
        print_game_board prints the game board in a readable way

        :return: None
        """
        print('\n')
        for row in self.game_board:
            print(row)
        print('\n')

    def get_move_count(self):
        return self.move_count
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

    def check_goal(self):
        """
        check_goal checks to see if the character token has reached the goal token

        :return: None
        """
        if self.check_placed() == 0:
            return False

        if self.char_loc[0] == self.goal_loc[0] and self.char_loc[1] == self.goal_loc[1]:
            self.game_board[self.char_loc[0]][self.char_loc[1]] = 'x'
            return True

    def check_placed(self):
        """
        check_placed checks to see if the character and goal tokens have been placed on game board

        :return: 0 if not placed, 1 if placed
        """
        if self.goal_loc[0] is None or self.goal_loc[1] is None:
            return False
        elif self.char_loc[0] is None or self.char_loc[1] is None:
            return False

        return True

    def move_left(self):
        """
        move_left moves the character token one space to the left on the game board if the move is valid.
        Each valid call increments self.move_count and update self.char_loc

        :return: None
        """
        # if either character or goal has not been placed, notify user and return
        if not self.check_placed():
            print("Character or goal has not yet been placed")
            return
        # if move causes character to go off the board, notify user and do nothing
        elif (self.char_loc[1]-1) < 0:
            print("Invalid move, please pick another path")
            return

        # reset prev location and move character token 1 space to the left
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'o'
        self.char_loc[1] = self.char_loc[1] - 1
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'c'
        # update mover counter and check if goal has been reached
        self.move_count += 1

    def move_right(self):
        """
        move_right moves the character token one space to the right on the game board if the move is valid.
        Each valid call increments self.move_count and update self.char_loc

        :return: None
        """
        # if either character or goal has not been placed, notify user and return
        if not self.check_placed():
            print("Character or goal has not yet been placed")
            return
        # if move causes character to go off the board, notify user and do nothing
        elif (self.char_loc[1]+1) >= self.board_size:
            print("Invalid move, please pick another path")
            return

        # reset prev location and move character token 1 space to the left
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'o'
        self.char_loc[1] = self.char_loc[1] + 1
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'c'
        # update mover counter and check if goal has been reached
        self.move_count += 1


    def move_up(self):
        """
        move_up moves the character token one space to the up on the game board if the move is valid.
        Each valid call increments self.move_count and update self.char_loc

        :return: None
        """
        # if either character or goal has not been placed, notify user and return
        if not self.check_placed():
            print("Character or goal has not yet been placed")
            return
        # if move causes character to go off the board, notify user and do nothing
        elif (self.char_loc[0]-1) < 0:
            print("Invalid move, please pick another path")
            return

        # reset prev location and move character token 1 space to the left
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'o'
        self.char_loc[0] = self.char_loc[0] - 1
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'c'
        # update mover counter and check if goal has been reached
        self.move_count += 1

    def move_down(self):
        """
        move_down moves the character token one space to the down on the game board if the move is valid.
         Each valid call increments self.move_count and update self.char_loc

        :return: None
        """
        # if either character or goal has not been placed, notify user and return
        if not self.check_placed():
            print("Character or goal has not yet been placed")
            return
        # if move causes character to go off the board, notify user and do nothing
        elif (self.char_loc[0]+1) >= self.board_size:
            print("Invalid move, please pick another path")
            return

        # reset prev location and move character token 1 space to the left
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'o'
        self.char_loc[0] = self.char_loc[0] + 1
        self.game_board[self.char_loc[0]][self.char_loc[1]] = 'c'
        # update mover counter and check if goal has been reached
        self.move_count += 1



if __name__ == '__main__':



    grid_size = int(input("Please input the size of the game board greater than 1 "))

    game = GameBoard(grid_size)
    goal_row = random.randint(0, grid_size - 1)
    goal_col = random.randint(0, grid_size - 1)

    # Generate a list of integers in the range [0, grid_size-1] excluding goal_row and goal_col
    excluded_rows = [goal_row]
    excluded_cols = [goal_col]
    all_rows = list(range(grid_size))
    all_cols = list(range(grid_size))
    possible_rows = list(set(all_rows) - set(excluded_rows))
    possible_cols = list(set(all_cols) - set(excluded_cols))

    # Choose random values for x and y from the possible ranges
    char_row = random.sample(possible_rows, 1)[0]
    char_col = random.sample(possible_cols, 1)[0]

    # Place the goal and character in their respective locations
    game.place_goal(goal_row, goal_col)
    game.place_character(char_row, char_col)

    while True:
        game.print_game_board()
        move = input("choose a direction to move (left, right, up, down) ")
        if move not in ["left", "right", "up", "down"]:
            print("Invalid input: please choose from the following (left, right, up, down) ")
            continue

        if move == "left":
            game.move_left()

        if move == "right":
            game.move_right()

        if move == "up":
            game.move_up()

        if move == "down":
            game.move_down()

        if game.check_goal():
            num_moves = game.get_move_count()
            print(f"Congratulations! You've reached the goal and it only took {num_moves} moves")
            break

