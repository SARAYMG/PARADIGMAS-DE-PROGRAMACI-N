class Robot:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.path = []
        self.visited = set()

    def find_path(self):
        if self.dfs(0, 0):
            return self.path
        else:
            return None

    def dfs(self, row, col):
        # Check boundaries and if cell is blocked or already visited
        if row >= self.rows or col >= self.cols or self.grid[row][col] == 1 or (row, col) in self.visited:
            return False

        # Add cell to visited set
        self.visited.add((row, col))

        # Add cell to path
        self.path.append((row, col))

        # If we have reached the bottom-right corner, return True
        if row == self.rows - 1 and col == self.cols - 1:
            return True

        # Move right
        if self.dfs(row, col + 1):
            return True

        # Move down
        if self.dfs(row + 1, col):
            return True

        # If neither right nor down works, backtrack
        self.path.pop()
        return False

# Ejemplo de uso:
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

robot = Robot(grid)
path = robot.find_path()

if path:
    print("Se encontró una ruta:", path)
else:
    print("No se encontró ninguna ruta")
