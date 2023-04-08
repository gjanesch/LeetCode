class Solution:
    """
    Checks the first cell's color, then queues up adjacent cells that
    haven't been checked already to check if they're the same color as
    image[sr][sc]'s original color, and change their color if so.

    The if statement at the beginning is used to catch the cases where
    you're changing a value to itself, so there's no point in running
    the rest of the code (no clue if that's a useful check in this
    sample problem).
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        value_to_change = image[sr][sc]
        if value_to_change == color:
            return image
        cells_to_check = [(sr, sc)]
        checked_cells = set()
        while cells_to_check:
            r, c = cells_to_check.pop(0)
            checked_cells.add((r, c))
            if image[r][c] == value_to_change:
                image[r][c] = color
                if r > 0 and (r-1, c) not in checked_cells:
                    cells_to_check.append((r-1, c))
                if r < m-1 and (r+1, c) not in checked_cells:
                    cells_to_check.append((r+1, c))
                if c > 0 and (r, c-1) not in checked_cells:
                    cells_to_check.append((r, c-1))
                if c < n-1 and (r, c+1) not in checked_cells:
                    cells_to_check.append((r, c+1))
        return image
