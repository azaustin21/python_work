from collections import deque
from typing import List
## Navigate a construction site and find obstacles
## on the construction site to dispose of.

def move_obstacle(lot: List[List[int]]) -> int:
    num_rows = len(lot)
    num_cols = len(lot[0])

    def get_neighbors(coord):
        row, col = coord
        for x_coord, y_coord in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            r_cell = row + x_coord
            c_cell = col + y_coord
            if 0 <= r_cell < num_rows and 0 <= c_cell < num_cols:
                yield (r_cell, c_cell)

    def breadth_first_search(start):
        queue = deque([start])
        r_cell, c_cell = start
        lot[r_cell][c_cell] = 0
        dist = 0
        while len(queue) > 0:
            dist += 1
            i = len(queue)
            for q in range(i):
                node = queue.popleft()
                for r_cell, c_cell in get_neighbors(node):
                    if lot[r_cell][c_cell] == 9:
                        return dist
                    if lot[r_cell][c_cell] == 0:
                        continue
                    queue.append((r_cell, c_cell))
                    lot[r_cell][c_cell] = 0

    return breadth_first_search((0, 0))

if __name__ == '__main__':
    lot = [[1, 0, 0], [1, 0, 0], [1, 9, 1]]
    res = move_obstacle(lot)
    print(res)


