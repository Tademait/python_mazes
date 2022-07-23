from cell import Cell
from grid import Grid
from binaryTree import BinaryTree

if __name__ == "__main__":
    grid = Grid(5, 5)
    BinaryTree().run(grid)
    print(grid)