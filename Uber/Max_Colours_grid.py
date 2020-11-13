class Grid:
    def __init__(self, grid):
        self.grid = grid

    def max_connected_colors(self):
        count = 0
        for i in grid:
            for j in i:
                if j == 1:
                    count += 1
                else:
                    continue
        return count


grid = [[1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 1, 0, 0]]

print(Grid(grid).max_connected_colors())
# 7
