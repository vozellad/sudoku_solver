from board import Board


def main():
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