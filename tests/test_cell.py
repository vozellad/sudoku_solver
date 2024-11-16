import pytest
from cell import Cell


def test_cell_initialization_with_number():
    """
    Test initialization of a Cell with a predefined number.
    """
    cell = Cell(5)
    assert cell.number == 5
    assert cell.candidates == []


def test_cell_initialization_without_number():
    """
    Test initialization of a Cell without a predefined number.
    """
    cell = Cell()
    assert cell.number is None
    assert cell.candidates == []


def test_add_candidate_to_empty_cell():
    """
    Test adding a candidate to an empty cell.
    """
    cell = Cell()
    cell.add_candidate(3)
    assert cell.candidates == [3]


def test_add_duplicate_candidate():
    """
    Test that adding a duplicate candidate does not add it again.
    """
    cell = Cell()
    cell.add_candidate(4)
    cell.add_candidate(4)
    assert cell.candidates == [4]


def test_remove_candidate_from_cell():
    """
    Test removing a candidate from the cell.
    """
    cell = Cell()
    cell.add_candidate(2)
    cell.add_candidate(5)
    cell.remove_candidate(2)
    assert cell.candidates == [5]


def test_remove_candidate_not_present():
    """
    Test removing a candidate that doesn't exist in the cell.
    """
    cell = Cell()
    cell.add_candidate(6)
    cell.remove_candidate(3)
    assert cell.candidates == [6]


def test_add_candidate_to_filled_cell():
    """
    Test adding a candidate to a cell with a fixed number.
    """
    cell = Cell(8)
    cell.add_candidate(3)
    assert cell.candidates == []
    assert cell.number == 8


def test_remove_candidate_from_filled_cell():
    """
    Test removing a candidate from a cell with a fixed number.
    """
    cell = Cell(7)
    cell.remove_candidate(7)
    assert cell.candidates == []
    assert cell.number == 7


def test_add_multiple_candidates():
    """
    Test adding multiple unique candidates to a cell.
    """
    cell = Cell()
    candidates = [1, 2, 3, 4]
    for candidate in candidates:
        cell.add_candidate(candidate)
    assert cell.candidates == candidates


def test_remove_all_candidates():
    """
    Test removing all candidates from a cell.
    """
    cell = Cell()
    candidates = [9, 8, 7]
    for candidate in candidates:
        cell.add_candidate(candidate)
    for candidate in candidates:
        cell.remove_candidate(candidate)
    assert cell.candidates == []
