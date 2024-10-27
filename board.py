"""
board.py - Sudoku Board Management Module

This module defines the `Board` class, which represents a 9x9 Sudoku board and contains methods to
manage the board's cells, find candidate numbers for empty cells, and apply solving techniques.
The `Board` class uses the `Cell` class from the `cell` module to represent each cell on the board.

Classes:
    - Board: Manages the layout and operations of a 9x9 Sudoku grid. It initializes from an input string
      representing the initial puzzle state and includes methods for finding possible values for each
      cell, based on Sudoku constraints within rows, columns, and 3x3 subgrids.

Key Methods:
    - __init__: Initializes the board with a provided string of 81 characters, where each character represents
      a cell's value or is a blank space (' ') for empty cells.
    - add_cell_num: Sets a specific number for a cell in the board.
    - output: Outputs the board’s current state to the console, showing numbers and blank spaces for empty cells.
    - find_candidates: Finds potential candidate values for each empty cell by eliminating values found in the
      same row, column, and 3x3 subgrid.
    - check_cell_row, check_cell_col, check_cell_box: Supporting methods for `find_candidates` that respectively
      eliminate candidates in the same row, column, and subgrid.
    - apply_mono_candidates: Sets the number for a cell if it has exactly one candidate, confirming it as the
      final value for that cell.

Usage:
    - Initialize a `Board` instance with an 81-character string to represent the starting state of the board.
    - Call `find_candidates()` to calculate possible candidates for each empty cell.
    - Use `apply_mono_candidates()` to fill in cells with a single candidate.
    - Use `output()` to display the current state of the board.

Example:
    ```python
    init_nums = "  1   5        4    6 8  139       4     3 6 8 7  1    42  76 1   5 2      41   7"
    board = Board(init_nums)
    board.find_candidates()
    board.apply_mono_candidates()
    board.output()
    ```

Dependencies:
    - cell: Contains the `Cell` class, which represents individual cells on the board, with attributes
      for the cell's number and potential candidates.
"""



from cell import Cell


class Board:
    """
    Represents a 9x9 Sudoku board with methods to manage cell numbers and candidate lists.

    Attributes:
        board (list of lists of Cell): A 2D list of Cell objects representing the board.
    """

    def __init__(self, init_nums: str):
        """
        Initializes the board using a string representing the initial numbers on the Sudoku board.

        Args:
            init_nums (str): An 81-character string where each character represents a cell's number,
                             with a space (' ') for empty cells.
        Raises:
            ValueError: If the input string is not exactly 81 characters.
        """
        if len(init_nums) != 81:
            raise ValueError('init_nums isn\'t 81 characters.')

        self.board = [[None] * 9 for _ in range(9)]
        for row in range(9):
            for col in range(9):
                curr_num = init_nums[row * 9 + col]
                if curr_num == ' ':
                    self.board[row][col] = Cell()
                else:
                    self.board[row][col] = Cell(curr_num)

    def add_cell_num(self, row, col, cell_num):
        """
        Sets a specific cell's number on the board.

        Args:
            row (int): Row index of the cell.
            col (int): Column index of the cell.
            cell_num (int): The number to set in the specified cell.
        """
        self.board[row][col].number = cell_num

    def output(self):
        """
        Prints the current state of the board in a readable format,
        with blank spaces for empty cells.
        """
        for b in self.board:
            print('[', end='')
            for cell in b:
                n = ' ' if cell.number is None else cell.number
                print(n, end='')
                if cell != b[-1]:
                    print(', ', end='')
            print(']')

    def find_candidates(self):
        """
        Finds all possible candidate numbers for each empty cell on the board by checking
        rows, columns, and 3x3 subgrids for conflicts.
        """
        for row in range(9):
            for col in range(9):
                cell = self.board[row][col]
                if cell.number is not None:
                    continue

                if cell.candidates == []:
                    for n in range(1, 10):
                        cell.add_candidate(n)

                self.check_cell_row(row, col, cell)
                self.check_cell_col(row, col, cell)
                self.check_cell_box(row, col, cell)


    def check_cell_row(self, row_of_cell, col_of_cell, cell):
        """
        Eliminates candidates for a cell based on numbers found in the same row.

        Args:
            row_of_cell (int): Row index of the cell being checked.
            col_of_cell (int): Column index of the cell being checked.
            cell (Cell): The cell whose candidates are being modified.
        """
        for col in range(9):
            if col == col_of_cell:
                continue

            curr_num = self.board[row_of_cell][col].number
            if curr_num is not None:
                cell.remove_candidate(curr_num)

    def check_cell_col(self, row_of_cell, col_of_cell, cell):
        """
        Eliminates candidates for a cell based on numbers found in the same column.

        Args:
            row_of_cell (int): Row index of the cell being checked.
            col_of_cell (int): Column index of the cell being checked.
            cell (Cell): The cell whose candidates are being modified.
        """
        for row in range(9):
            if row == row_of_cell:
                continue

            curr_num = self.board[row][col_of_cell].number
            if curr_num is not None:
                cell.remove_candidate(curr_num)

    def check_cell_box(self, row_of_cell, col_of_cell, cell):
        """
        Eliminates candidates for a cell based on numbers
        found in the 3x3 subgrid containing the cell.

        Args:
            row_of_cell (int): Row index of the cell being checked.
            col_of_cell (int): Column index of the cell being checked.
            cell (Cell): The cell whose candidates are being modified.
        """
        row_start = row_of_cell // 3 * 3
        col_start = col_of_cell // 3 * 3
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if row == row_of_cell and col == col_of_cell:
                    continue

                curr_num = self.board[row][col].number
                if curr_num is not None:
                    cell.remove_candidate(curr_num)

    def apply_mono_candidates(self):
        """
        Sets the cell's number if it has exactly one candidate, thus determining its final value.
        """
        for b in self.board:
            for cell in b:
                if cell.number is None and len(cell.candidates) == 1:
                    cell.number = cell.candidates[0]
