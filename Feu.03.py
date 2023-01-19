import numpy as np

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == ".":
                return (i, j)
    return None

def is_valid(grid, num, pos):
    for i in range(9):
        if grid[pos[0]][i] == num or grid[i][pos[1]] == num:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if grid[i][j] == num:
                return False
    return True

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find
    for num in range(1,10):
        if is_valid(grid, str(num), (row, col)):
            grid[row][col] = str(num)
            if solve(grid):
                return True
            grid[row][col] = "."
    return False

if __name__ == "__main__":
    grid = []
    with open("s.txt", "r") as f: # ouvrir le fichier
        for line in f:
            grid.append(list(line.strip()))
    solve(grid)
    print(np.matrix(grid))
