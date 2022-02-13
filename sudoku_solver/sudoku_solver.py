"""
    Creator: 0nyx_Ch4rm
    Date: 2.12.2022
    Description: Building an auto soduku solver
"""
import enum
from typing import List

from loguru import logger

# Rows separated by commas
EASY = (
    "000030640030705800820096070000070296003429010298561407702900000000000064459000700"
)
# MEDIUM =
# HARD =
SOLVED = (
    "128653947973284165546179823435891672862735419719426358657948231394512786281367594"
)
PUZZLES = {"easy": EASY, "solved": SOLVED}
# TODO: create a function for random boards


def load_board(difficulty: str) -> List[List[int]]:
    """This function will load a sudoku board into the game."""
    # TODO: could allow for user input
    board = [[0 for _ in range(9)] for _ in range(9)]
    if difficulty in PUZZLES:
        puzzle = PUZZLES[difficulty]
    else:
        puzzle = PUZZLES["easy"]

    for row in range(9):
        for col in range(9):
            board[row][col] = int(puzzle[row * 9 + col])

    return board


def print_board(board):
    """Prints the board out"""
    for row in board:
        for column in row:
            print(column, end="")
        print()


def validate_board(board):
    """Checks the board to see if complete and correct"""

    def _validate_line(row):
        "Give a list of row or column number validates it"
        if 0 in row:
            return False
        for num in range(1, 10):
            if num not in row:
                logger.debug(f"{num} not in {row}")
                return False
        return True

    def _validate_square(board, row_start, col_start):
        square_nums = []
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                square_nums.append(board[row][col])
        return _validate_line(square_nums)

    # Validate Rows
    for row in board:
        if not _validate_line(row):
            logger.error(f"Row Failed Validation: {row}")
            return False

    # Validate Columns
    for col in range(9):
        if not _validate_line(t_col := [board[row][col] for row in range(9)]):
            logger.error(f"Columns Failed Validation: {t_col}")
            return False

    # Validate Squares
    for row in range(3):
        for col in range(3):
            if not _validate_square(board, row * 3, col * 3):
                logger.error("Squares Failed Validation")
                return False
    return True


def guess_in_column(board, column, guess):
    """Checks to see if the guess is in the column"""
    return any([board[row][column] == guess for row in range(9)])


def guess_in_row(board, row, guess):
    """Checks to see if the guess is in the row"""
    return any([board[row][column] == guess for column in range(9)])


def guess_in_square(board, row, column, guess):
    """Validates that a 3x3 square has no errors"""
    row_start = row // 3 * 3
    column_start = column // 3 * 3

    for i_row in range(row_start, row_start + 3):
        for i_col in range(column_start, column_start + 3):
            if board[i_row][i_col] == guess:
                return True
    return False


def check_guess(board, row, column, guess):
    if guess_in_column(board, column, guess):
        # logger.debug(f"Failed column guess ({row}, {column}) = {guess}")
        return False
    if guess_in_row(board, row, guess):
        # logger.debug(f"Failed row guess ({row}, {column}) = {guess}")
        return False
    if guess_in_square(board, row, column, guess):
        # logger.debug(f"Failed guess ({row}, {column}) = {guess}")
        return False
    return True


def find_empty_space(board):
    for r_index, row in enumerate(board):
        for c_index, col in enumerate(row):
            if col == 0:
                return (r_index, c_index)


def solve(board):
    # logger.debug(print_board(board))
    open_space = find_empty_space(board)

    if not open_space:
        logger.warning("NO EMPTY SPACES FOUND")
        if validate_board(board):
            return True, board
        else:
            logger.critical("Solver was not able to solve puzzle")
            return False, board
    else:
        row, col = open_space
        # logger.debug(f"Empty space at ({row},{col})")

    for guess in range(1, 10):
        if check_guess(board, row, col, guess):
            board[row][col] = guess

            status, board = solve(board)
            if status:
                return True, board

            board[row][col] = 0

    return False, board


board = load_board("easy")
print_board(board)
status, board = solve(board)

if status:
    print("Solved Sudoku Puzzle!!!!")
    print_board(board)
else:
    print("Failed to solve board")
