"""
Test basic functionality of the maze library
"""
import pytest
from ..src.cell import Cell
from ..src.grid import Grid


def test_cell_init():
    cella = Cell(2, 3)
    assert not cella.linked()

def test_link_two_bidi():
    cell1 = Cell(2, 3)
    cell2 = Cell(3, 3)
    cell1.link(cell2)
    print(cell1)
    print(cell1.linked())
    assert cell2 in cell1.linked()
    assert cell1 in cell2.linked()

def test_link_not_bidi():
    cell1 = Cell(2, 3)
    cell2 = Cell(3, 3)
    cell1.link(cell2, False)
    assert cell2 in cell1.linked()
    assert cell1 not in cell1.linked()

def test_unlink_cell():
    cell1 = Cell(2, 3)
    cell2 = Cell(3, 3)
    cell1.link(cell2)
    cell1.unlink(cell2)
    assert cell2 not in cell1.linked()
    assert cell1 not in cell2.linked()

def test_unlink_cell_bidi():
    cell1 = Cell(2, 3)
    cell2 = Cell(3, 3)
    cell1.link(cell2)
    cell2.unlink(cell1)
    assert cell2 not in cell1.linked()
    assert cell1 not in cell2.linked()

def test_is_linked_to():
    cell1 = Cell(2, 3)
    cell2 = Cell(3, 3)
    assert not cell1.is_linked_to(cell2)
    cell1.link(cell2)
    assert cell1.is_linked_to(cell2)

def test_query_neighbors():
    cell1 = Cell(2, 3)
    cell2 = Cell(3, 3)
    assert not cell1.neighbors()
    cell1.link(cell2)
    # todo n/s/e/w neighbors are managed by grid module, cant test now

def test_grid_init():
    grid1 = Grid(2, 2)
    for i in range(grid1.rows):
        print()
        for j in range(grid1.columns):
            print(grid1.grid[i][j], end=" ")
    assert True

def test_configure_cells():
    #  0;0  0;1
    #  1;0  1;1

    grid1 = Grid(2, 2)
    top_left_cell = grid1.grid[0][0]
    assert top_left_cell.north == None
    assert top_left_cell.south == grid1.grid[1][0]
    assert top_left_cell.west == None
    assert top_left_cell.east == grid1.grid[0][1]

    top_right_cell = grid1.grid[0][1]
    assert top_right_cell.north == None
    assert top_right_cell.south == grid1.grid[1][1] 
    assert top_right_cell.west == grid1.grid[0][0]
    assert top_right_cell.east == None

def test_get_size():
    grid1 = Grid(2, 2)
    grid_size = grid1.get_size()
    assert grid_size == 4
