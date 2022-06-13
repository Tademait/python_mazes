"""
Test basic functionality of the maze library
"""
import pytest
from cell import Cell


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



