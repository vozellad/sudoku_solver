class Cell:
    def __init__(self, number=None):
        self.number = number
        self.candidates = []

    def add_candidate(self, new_candidate):
        if new_candidate not in self.candidates:
            self.candidates.append(new_candidate)
        else:
            print(f'Candidate {new_candidate} already in list.')

    def remove_candidate(self, candidate):
        if candidate in self.candidates:
            self.candidates.remove(candidate)


class Board:
    def __init__(self, init_nums: str):
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
        self.board[row][col].number = cell_num

    def output(self):
        for b in self.board:
            print('[', end='')
            for cell in b:
                n = ' ' if cell.number is None else cell.number
                print(n, end='')
                if cell != b[-1]:
                    print(', ', end='')
            print(']')

    def find_candidates(self):
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
        for col in range(9):
            if col == col_of_cell:
                continue

            curr_num = self.board[row_of_cell][col].number
            if curr_num is not None:
                cell.remove_candidate(curr_num)

    def check_cell_col(self, row_of_cell, col_of_cell, cell):
        for row in range(9):
            if row == row_of_cell:
                continue

            curr_num = self.board[row][col_of_cell].number
            if curr_num is not None:
                cell.remove_candidate(curr_num)

    def check_cell_box(self, row_of_cell, col_of_cell, cell):
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
        for b in self.board:
            for cell in b:
                if cell.number is None and len(cell.candidates) == 1:
                    cell.number = cell.candidates[0]


def main():
    init_nums = "  1   5        4    6 8  139       4     3 6 8 7  1    42  76 1   5 2      41   7"
    board = Board(init_nums)

    # go through methods of finding cell numbers until the board is completed
    while True:
        board.find_candidates()
        print()
        board.apply_mono_candidates()

        board.output()
        break


main()