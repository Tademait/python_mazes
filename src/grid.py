from src.cell import Cell
from random import randint

class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.grid = self.prepare_grid()
        self.configure_cells()

    def __repr__(self):
        output = "+" + "---+" * self.columns + "\n"
        


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
