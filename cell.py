"""
cell.py - Sudoku Cell Representation Module

This module defines the `Cell` class, which represents an individual cell in a Sudoku puzzle grid. Each
cell can contain a set number (if already determined) or a list of candidate numbers if the cell is empty.
The class provides methods for managing candidate numbers, allowing the addition or removal of possible values.

Classes:
    - Cell: Represents a single cell on the Sudoku board, managing its value and potential candidates
      if the cell is empty.

Key Attributes:
    - number: Stores the fixed value of the cell, if known; otherwise, remains `None`.
    - candidates: A list of potential numbers that may be valid for the cell, useful when deducing cell values.

Key Methods:
    - __init__: Initializes the cell with an optional number. If no number is provided, initializes an empty
      list for candidate numbers.
    - add_candidate: Adds a new candidate number to the cell's list if it’s not already present.
    - remove_candidate: Removes a specified candidate from the cell's list if it’s present.

Usage:
    - Initialize a `Cell` with or without a starting number.
    - Use `add_candidate` to add potential values, especially during puzzle-solving processes where the final
      value is not yet known.
    - Use `remove_candidate` to eliminate impossible values based on Sudoku constraints in rows, columns,
      and subgrids.

Example:
    ```python
    cell = Cell()
    cell.add_candidate(5)
    cell.remove_candidate(5)
    cell.number = 9
    ```

Dependencies:
    - None
"""


class Cell:
    """
    Represents an individual cell in a Sudoku board. Each cell can have a number (if already set) or
    a list of possible candidates (if the cell is empty).

    Attributes:
        number (int or None): The current number in the cell, or None if the cell is empty.
        candidates (list of int): Potential numbers that could be valid for this cell.
    """

    def __init__(self, number: int=None):
        """
        Initializes a cell with an optional number. If the cell is empty,
        it initializes an empty list for candidates.

        Args:
            number (int or None): The initial number for the cell, or None if the cell is empty.
        """
        self.number = number
        self.candidates = []  # TODO: change to set

    def add_candidate(self, new_candidate: int):
        """
        Adds a candidate number to the cell if it's not already in the list.

        Args:
            new_candidate (int): A candidate number to add to the cell.
        """
        if new_candidate not in self.candidates:
            self.candidates.append(new_candidate)
        else:
            print(f'Candidate {new_candidate} already in list.')

    def remove_candidate(self, candidate: int):
        """
        Removes a candidate number from the cell if it exists in the list.

        Args:
            candidate (int): The candidate number to remove.
        """
        if candidate in self.candidates:
            self.candidates.remove(candidate)
