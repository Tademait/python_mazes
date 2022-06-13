class Cell:
    def __repr__(self):
        return f"<Cell object|r{self.row} c{self.column}"

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.links = dict()

        self.north = None
        self.south = None
        self.west = None
        self.east = None

    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi=True):
        del self.links[cell]
        if bidi:
            cell.unlink(self, False)

    def linked(self):
        return list(self.links.keys())

    def is_linked_to(self, cell):
        return cell in self.links.keys()

    def neighbors(self):
        neighbor_list = []
        if self.north:
            neighbor_list.append(north)
        if self.south:
            neighbor_list.append(south)
        if self.west:
            neighbor_list.append(west)
        if self.east:
            neighbor_list.append(east)
        return neighbor_list


        