from cell import Cell
from grid import Grid
from binaryTree import BinaryTree
from sidewinder import Sidewinder


if __name__ == "__main__":
    grid: Grid = Grid(5, 5)
    print(Sidewinder().run(grid))
