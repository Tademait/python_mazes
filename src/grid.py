from cell import Cell

class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.grid = prepare_grid()
        configure_cells()

    def prepare_grid(self):
        for row in range(self.rows):
            for col in range(self.columns):
                Cell(row, col)

    def configure_cells(self):
        raise NotImplementedError