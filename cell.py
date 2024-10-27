class Cell:
    """
    Represents an individual cell in a Sudoku board. Each cell can have a number (if already set) or
    a list of possible candidates (if the cell is empty).

    Attributes:
        number (int or None): The current number in the cell, or None if the cell is empty.
        candidates (list of int): Potential numbers that could be valid for this cell.
    """

    def __init__(self, number=None):
        """
        Initializes a cell with an optional number. If the cell is empty,
        it initializes an empty list for candidates.

        Args:
            number (int or None): The initial number for the cell, or None if the cell is empty.
        """
        self.number = number
        self.candidates = []

    def add_candidate(self, new_candidate):
        """
        Adds a candidate number to the cell if it's not already in the list.

        Args:
            new_candidate (int): A candidate number to add to the cell.
        """
        if new_candidate not in self.candidates:
            self.candidates.append(new_candidate)
        else:
            print(f'Candidate {new_candidate} already in list.')

    def remove_candidate(self, candidate):
        """
        Removes a candidate number from the cell if it exists in the list.

        Args:
            candidate (int): The candidate number to remove.
        """
        if candidate in self.candidates:
            self.candidates.remove(candidate)
