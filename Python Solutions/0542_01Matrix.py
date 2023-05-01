class Solution:
    """
    Unsophisticated (i.e., non-dynamic) method.  Starting from the list
    of cells with zeroes, find any adjacent cells that don't already
    have values, and give them a value of 1.  The find anything
    adjacent to those, give them value 2, and so forth.
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m, n = len(mat), len(mat[0])
        cells_with_distances = set()
        distances = [[None]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    cells_with_distances.add((i,j))
                    distances[i][j] = 0

        last_batch = cells_with_distances
        current_distance = 0

        while len(cells_with_distances) < m*n:
            current_distance = current_distance + 1
            new_batch = set()
            for cell in last_batch:
                adjacent_cells = self.get_adjacent_cells(*cell, m, n)
                for ac in adjacent_cells:
                    if ac not in cells_with_distances and ac not in last_batch:
                        distances[ac[0]][ac[1]] = current_distance
                        new_batch.add(ac)
            cells_with_distances.update(last_batch)
            last_batch = new_batch

        return distances

    def get_adjacent_cells(self, i, j, m, n):
        adjacent_cells = []
        if i > 0:
            adjacent_cells.append((i-1,j))
        if i < m-1:
            adjacent_cells.append((i+1,j))
        if j > 0:
            adjacent_cells.append((i,j-1))
        if j < n-1:
            adjacent_cells.append((i,j+1))
        return adjacent_cells
