from cell import Cell
from grid import Grid
from random import randint

class Sidewinder:
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
            run = []

            cell: Cell
            for cell in row:
                run.append(cell)

                at_eastern_boundary = (cell.east == None)
                at_northern_boundary = (cell.north == None)

                should_close_out = at_eastern_boundary or (
                    not at_northern_boundary and randint(0, 2) == 0
                )

                if should_close_out:
                    member: Cell = run[randint(0, len(run) - 1)]
                    if member.north:
                        member.link(member.north)
                    run = []
                else:
                    cell.link(cell.east)
        return grid_copy
