from cell import Cell
from grid import Grid
from random import randint

class BinaryTree:
    @staticmethod
    def run(grid):
        """Applies a maze-making algortihm

        Args:
            grid (Grid): The grid you want to apply the algorithm to

        Returns:
            Grid: Returns modified version of the grid with applied maze-making 
            algorithm
        """
        grid_copy = grid
        for row in grid_copy.grid:
            for cell in row:
                neighbors = []
                if cell.north:
                    neighbors.append(cell.north)
                if cell.east:
                    neighbors.append(cell.east)

                if neighbors:
                    cell.link(neighbors[randint(0, len(neighbors) - 1)])
        return grid_copy