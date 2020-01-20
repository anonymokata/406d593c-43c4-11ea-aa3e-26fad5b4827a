import unittest
from pencil_durability import Paper, Pencil


class TestEraser(unittest.TestCase):
    def test_that_eraser_erases_last_occurance_of_text_on_paper(self):
        point_durability = 50
        initial_length = 5
        pencil = Pencil(point_durability=point_durability, initial_length=initial_length)
        paper = Paper()
        pencil.write(paper, 'test the eraser test the eraser')
        pencil.erase(paper, 'eraser')
        self.assertEqual('test the eraser test the       ', paper.display_page())


if __name__ == '__main__':
    unittest.main()
