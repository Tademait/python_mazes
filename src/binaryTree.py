from cell import Cell
from grid import Grid
from random import randint

class BinaryTree:
    @staticmethod
    def run(grid):
        for row in grid.grid:
            for cell in row:
                neighbors = []
                if cell.north:
                    neighbors.append(cell.north)
                if cell.east:
                    neighbors.append(cell.east)

                if neighbors:
                    cell.link(neighbors[randint(0, len(neighbors) - 1)])
