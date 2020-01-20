import unittest
from Eraser import Eraser
from Paper import Paper
from Pencil import Pencil


class TestEraser(unittest.TestCase):
    def test_that_eraser_erases_last_occurance_of_text_on_paper(self):
        point_durability = 50
        initial_length = 5
        pencil = Pencil(point_durability=point_durability, initial_length=initial_length)
        paper = Paper()
        pencil.write(paper, 'test the eraser test the eraser')
        pencil.erase(paper, 'eraser')
        self.assertEqual('test the eraser test the       ', paper.display_page())

    def test_that_eraser_can_be_initialized_with_a_durability(self):
        durability = 10
        eraser = Eraser(durability=durability)
        self.assertEqual(10, eraser.durability)


if __name__ == '__main__':
    unittest.main()
