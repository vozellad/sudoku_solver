import pytest
from board import Board
from cell import Cell


def test_board_initialization():
    # Test 81-character string for correct initialization
    init_nums = "  1   5        4    6 8  139       4     3 6 8 7  1    42  76 1   5 2      41   7"
    board = Board(init_nums)

    # Check that each cell was initialized correctly
    assert len(board.board) == 9
    for row in board.board:
        assert len(row) == 9
        for cell in row:
            assert isinstance(cell, Cell)

    # Check for specific values based on init_nums string
    assert board.board[0][2].number == '1'
    assert board.board[0][6].number == '5'
    assert board.board[1][6].number == '4'
    assert board.board[8][8].number == '7'


def test_board_invalid_init_length():
    # Test ValueError for input not 81 characters long
    with pytest.raises(ValueError):
        Board("123")  # Shorter string should raise ValueError


def test_board_empty_cells():
    # Test that empty cells are initialized with None in their number attribute
    init_nums = " " * 81
    board = Board(init_nums)

    for row in board.board:
        for cell in row:
            assert cell.number is None  # Each cell should have None as its number for empty cells


def test_board_filled_cells():
    # Test that filled cells are initialized with their numbers from init_nums
    init_nums = "1" * 81
    board = Board(init_nums)

    for row in board.board:
        for cell in row:
            assert cell.number == '1'  # Each cell should have '1' as its number


def test_add_cell_num():
    # Initialize a board with an empty string to start with a blank board
    init_nums = " " * 81
    board = Board(init_nums)

    # Add a number to a specific cell and check if it's set correctly
    board.add_cell_num(0, 0, '5')
    assert board.board[0][0].number == '5'

    board.add_cell_num(8, 8, '9')
    assert board.board[8][8].number == '9'

    board.add_cell_num(4, 4, '7')
    assert board.board[4][4].number == '7'

    board.add_cell_num(0, 8, '2')
    assert board.board[0][8].number == '2'

    board.add_cell_num(8, 0, '6')
    assert board.board[8][0].number == '6'

    # Replace number
    board.add_cell_num(8, 8, '9')
    assert board.board[8][8].number == '9'

    board.add_cell_num(0, 8, '7')
    assert board.board[0][8].number == '7'


def test_output_empty_board(capfd):
    # Test the output of an empty board
    init_nums = " " * 81
    board = Board(init_nums)

    board.output()

    captured = capfd.readouterr()

    expected_output = (
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
    )

    assert captured.out == expected_output


def test_output_partial_board(capfd):
    # Test the output of a partially filled board
    init_nums = "54678912 " + " " * 72
    board = Board(init_nums)

    board.output()

    captured = capfd.readouterr()

    expected_output = (
        "[5, 4, 6, 7, 8, 9, 1, 2,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
        "[ ,  ,  ,  ,  ,  ,  ,  ,  ]\n"
    )

    assert captured.out == expected_output


def test_output_filled_board(capfd):
    # Test the output of a fully filled board
    init_nums = "123456789" * 9
    board = Board(init_nums)

    board.output()  # Call the output method

    captured = capfd.readouterr()

    expected_output = (
        "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
        "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
        "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
        "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
        "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
        "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
        "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
        "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
        "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
    )

    assert captured.out == expected_output


def test_find_candidates_empty_board():
    init_nums = " " * 81  # All cells are empty
    board = Board(init_nums)

    board.find_candidates()

    for row in range(9):
        for col in range(9):
            cell = board.board[row][col]
            # Each empty cell should have candidates from 1 to 9
            assert set(cell.candidates) == set(range(1, 10))


def test_find_candidates_full_board():
    init_nums = "123456789" * 9
    board = Board(init_nums)

    board.find_candidates()

    for row in range(9):
        for col in range(9):
            cell = board.board[row][col]
            assert cell.candidates == []


def test_check_cell_row_empty_row():
    board = Board(' ' * 81)
    board.board[0][0].candidates = list(range(1, 10))
    board.check_cell_row(0, 0, board.board[0][0])
    assert set(board.board[0][0].candidates) == set(range(1, 10))


def test_check_cell_row_with_numbers():
    init_nums = '12 456 89' + ' ' * 72
    board = Board(init_nums)
    board.board[0][2].candidates = list(range(1, 10))
    board.check_cell_row(0, 2, board.board[0][2])
    assert set(board.board[0][2].candidates) == {3, 7}


def test_check_cell_col_empty_col():
    board = Board(' ' * 81)
    board.board[0][0].candidates = list(range(1, 10))
    board.check_cell_col(0, 0, board.board[0][0])
    assert set(board.board[0][0].candidates) == set(range(1, 10))


def test_check_cell_col_with_numbers():
    init_nums = f"1{' '*8}2{' '*8}{' '*9}4{' '*8}5{' '*8}6{' '*8}{' '*9}8{' '*8}9{' '*8}"
    board = Board(init_nums)
    board.board[2][0].candidates = list(range(1, 10))
    board.check_cell_col(2, 0, board.board[2][0])
    assert set(board.board[2][0].candidates) == {3, 7}


def test_check_cell_box_empty_box():
    board = Board(' ' * 81)
    board.board[1][1].candidates = list(range(1, 10))
    board.check_cell_box(1, 1, board.board[1][1])
    assert set(board.board[1][1].candidates) == set(range(1, 10))


def test_check_cell_box_with_numbers():
    init_nums = f"1 3{' '*6}4 6{' '*6}789{' '*60}"
    board = Board(init_nums)
    board.board[1][1].candidates = list(range(1, 10))
    board.check_cell_box(1, 1, board.board[1][1])
    assert set(board.board[1][1].candidates) == {2, 5}


def test_apply_mono_candidates_no_candidates():
    board = Board(' ' * 81)

    for row in board.board:
        for cell in row:
            cell.candidates = []

    board.apply_mono_candidates()

    for row in board.board:
        for cell in row:
            assert cell.number is None


def test_apply_mono_candidates_with_single_candidate():
    board = Board(' ' * 81)

    board.board[0][0].candidates = [3]
    board.board[1][1].candidates = [5]
    board.board[2][2].candidates = [7]

    board.apply_mono_candidates()

    assert board.board[0][0].number == 3
    assert board.board[1][1].number == 5
    assert board.board[2][2].number == 7

    for row in range(9):
        for col in range(9):
            if (row, col) not in [(0, 0), (1, 1), (2, 2)]:
                assert board.board[row][col].number is None


def test_apply_mono_candidates_with_multiple_candidates():
    board = Board(' ' * 81)

    board.board[0][0].candidates = [1, 2, 3]
    board.board[1][1].candidates = [4, 5, 6]
    board.board[2][2].candidates = [7, 8, 9]

    board.apply_mono_candidates()

    for row in board.board:
        for cell in row:
            assert cell.number is None


def test_apply_mono_candidates_mixed():
    board = Board(' ' * 81)

    board.board[0][0].candidates = [9]
    board.board[2][2].candidates = [1, 2, 3]

    board.apply_mono_candidates()

    assert board.board[0][0].number == 9
    assert board.board[2][2].number is None


def test_apply_mono_candidates_full_board():
    board = Board(' ' * 81)

    for row in board.board:
        for cell in row:
            cell.candidates = [5]

    board.apply_mono_candidates()

    for row in board.board:
        for cell in row:
            assert cell.number == 5
