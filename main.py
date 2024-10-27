"""
main.py - Sudoku Solver Main Execution File

This file provides the entry point for running the Sudoku puzzle solver. It initializes the Sudoku board
using the `Board` class (imported from the `board` module) and applies logical deduction methods to solve
the puzzle progressively. <methods have not been completed>

Modules:
    - board: Contains the `Board` class, which represents the 9x9 Sudoku board and includes methods
      to manage cell values, find candidates, and apply solving techniques.

Functions:
    - main(): Initializes the board from a given puzzle string, iteratively finds possible values
      for empty cells.

Usage:
    - Run this file to execute the solver. The initial puzzle configuration is represented by the
      `init_nums` string within `main()`, where each character corresponds to a cell, with spaces
      (' ') for empty cells.

Example:
    Input: A predefined string with 81 characters representing the initial Sudoku puzzle layout.
    Output: Console output of the board state after having found every number.
"""


from board import Board


def main():
    """
    Initializes Sudoku board. Loops through methods to find values until board is completed.
    """
    init_nums = "  1   5        4    6 8  139       4     3 6 8 7  1    42  76 1   5 2      41   7"
    board = Board(init_nums)

    # go through methods of finding cell numbers until the board is completed
    while True:
        board.find_candidates()
        print()
        board.apply_mono_candidates()

        board.output()
        break  # temporary code


main()
