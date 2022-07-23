from cell import Cell
from random import randint

class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.grid = self.prepare_grid()
        self.configure_cells()

    def __repr__(self):
        output = "+" + "---+" * self.columns + "\n"
        
        # todo: remove index & enumerate for clean output
        for index, row in enumerate(self.grid):
            top = "|"
            bottom = "+"

            for index2, cell in enumerate(row):

                # body = f"{index}x{index2}" # three spaces
                body = "   "
                east_boundary = " " if cell.is_linked_to(cell.east) else "|"
                top += body + east_boundary

                south_boundary = "   " if cell.is_linked_to(cell.south) else "---"
                corner = "+"
                bottom += south_boundary + corner

            output += top + "\n" + bottom + "\n"

        return output

    def prepare_grid(self):
        return [[Cell(row, col) for col in range(self.columns)] for row in range(self.rows)]

    def configure_cells(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if row > 0:
                    self.grid[row][col].north = self.grid[row - 1][col]                
                if row < self.rows - 1:
                    self.grid[row][col].south = self.grid[row + 1][col]
                if col > 0:
                    self.grid[row][col].west = self.grid[row][col - 1]
                if col < self.columns - 1:
                    self.grid[row][col].east = self.grid[row][col + 1]
    
    def get_random_cell(self):
        row = randint(0, self.rows)
        col = randint(0, self.columns)
        return self.grid[row][col]

    def get_size(self):
        return self.rows * self.columns
