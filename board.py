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
        Prints the current state of the board in a readable format, with blank spaces for empty cells.
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
                    [cell.add_candidate(n) for n in range(1, 10)]

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
        Eliminates candidates for a cell based on numbers found in the 3x3 subgrid containing the cell.

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
