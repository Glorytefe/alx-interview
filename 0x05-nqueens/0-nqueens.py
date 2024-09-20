#!/usr/bin/python3
"""
N-Queens Problem
- Solution Strategy: Backtracking
    - Implement backtracking to explore all potential configurations.
    - Validate the current configuration:
        - Ensure the column does not contain another queen.
        - Confirm no conflicts along the positive diagonal.
        - Confirm no conflicts along the negative diagonal.
    - Place the queen at the valid position on the board.
    - If the configuration is valid, continue to the next row until the board is fully populated.
    - If the configuration becomes invalid, backtrack and explore alternative placements.
    - Record the valid configuration if the end of the board is reached.
- Complexity Analysis:
    - Time Complexity: O(n!) - where n is the number of queens.
        - Initially, there are n options for the first queen, n - 1 for the second, n - 2 for the third, and so on.
    - Space Complexity: O(n^2) - where n represents the board size.
"""

import sys


def n_queens(n):
    """ N queens solution """
    queens_positions, solutions = [], []
    columns, pos_diagonals, neg_diagonals = set(), set(), set()

    def solve(row, n, queens_positions):
        """ Recursive function to find solutions """
        if row == n:
            solutions.append(queens_positions[:])
            return
        for col in range(n):
            if (col in columns or row + col in pos_diagonals or
                    row - col in neg_diagonals):
                continue
            columns.add(col)
            pos_diagonals.add(row + col)
            neg_diagonals.add(row - col)
            queens_positions.append([row, col])
            solve(row + 1, n, queens_positions)

            columns.remove(col)
            pos_diagonals.remove(row + col)
            neg_diagonals.remove(row - col)
            queens_positions.pop()

    solve(0, n, queens_positions)
    return solutions


def validate_input(n):
    """ Validate if the input argument is correct """
    if not n.isdigit():
        print("N must be a number")
        exit(1)
    if int(n) < 4:
        print("N must be at least 4")
        exit(1)


def main():
    """ Main function """
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        exit(1)
    n = args[1]
    validate_input(n)
    solutions = n_queens(int(n))
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
