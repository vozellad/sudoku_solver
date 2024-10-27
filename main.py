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
    def __init__(self):
        self.board = [[None] * 9 for _ in range(9)]
        for row in range(9):
            for col in range(9):
                self.board[row][col] = Cell()

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
    board = Board()
    init_nums = [
        (0, 2, 1), (0, 6, 5), (1, 6, 4), (2, 2, 6), (2, 4, 8), (2, 7, 1),
        (2, 8, 3), (3, 0, 9), (3, 8, 4), (4, 5, 3), (4, 7, 6), (5, 0, 8),
        (5, 2, 7), (5, 5, 1), (6, 1, 4), (6, 2, 2), (6, 5, 7), (6, 6, 6),
        (6, 8, 1), (7, 3, 5), (7, 5, 2), (8, 3, 4), (8, 4, 1), (8, 8, 7)
    ]
    for row, col, num in init_nums:
        board.add_cell_num(row, col, num)

    # go through methods of finding cell numbers until the board is completed
    while True:
        board.find_candidates()
        print()
        board.apply_mono_candidates()

        board.output()
        break


main()