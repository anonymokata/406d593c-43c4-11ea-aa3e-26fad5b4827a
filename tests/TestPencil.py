import unittest
from pencil_durability import Paper, Pencil


class TestPencil(unittest.TestCase):

    def test_that_pencil_writes_on_paper(self):
        paper = Paper()
        pencil = Pencil()
        pencil.write(paper, 'She sells sea shells')
        self.assertEqual('She sells sea shells', paper.display_page())

    def test_that_pencil_writes_where_it_left_off(self):
        paper = Paper()
        pencil = Pencil()
        pencil.write(paper, 'She sells sea shells')
        pencil.write(paper, ' down by the sea shore')
        self.assertEqual('She sells sea shells down by the sea shore', paper.display_page())

    def test_that_point_durability_can_be_set_on_construction(self):
        point_durability = 10
        pencil = Pencil(point_durability=point_durability)
        self.assertEqual(point_durability, pencil.point_durability)


if __name__ == '__main__':
    unittest.main()
