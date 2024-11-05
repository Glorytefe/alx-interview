#!/usr/bin/python3
 
def island_perimeter(grid):
    """
    Args:
        grid (list): A list of lists representing an island.
        0 - water, 1 - land
    Returns: 
        the perimeter of an island (grid).
    """
    height = len(grid)
    width = len(grid[0])
    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Subtract sides shared with adjacent land cells
                if i > 0 and grid[i - 1][j] == 1:  # Check above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    perimeter -= 2

    return perimeter
