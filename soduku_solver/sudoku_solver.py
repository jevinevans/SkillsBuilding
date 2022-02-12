"""
    Creator: 0nyx_Ch4rm
    Date: 2.12.2022
    Description: Building an auto soduku solver
"""
from typing import List
# Rows separated by commas
EASY = "000030640,030705800,820096070,000070296,003429010,298561407,702900000,000000064,459000700"
# MEDIUM = 
# HARD = 
PUZZLES = {"easy":EASY}
# TODO: create a function for random boards

def load_board(difficulty:str) -> List[List[int]]:
    """This function will load a sudoku board into the game."""
    # TODO: could allow for user input
    board = []
    if difficulty in PUZZLES:
        puzzle = PUZZLES[difficulty]
    else:
        puzzle = PUZZLES["easy"]

    for r_index, row in enumerate(puzzle.split(",")):
        board[r_index] = []
        for c_index, column in enumerate(row):
            board[r_index][c_index] = column
    
    return board

def validate_board():
    """Checks the board to make sure that it is still in a proper and there are not erros"""

    def _validate_column():
        """Validates that a column has no duplicates"""

    def _validate_row():
        """Validates that a row has no duplicates"""
    
    def _validate_square():
        """Validates that a 3x3 square has no errors"""

master_board = load_board('easy')
print(master_board)