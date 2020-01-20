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

    def test_that_eraser_degrades_correct_amount_for_non_whitespace_characters(self):
        durability = 10
        eraser = Eraser(durability=durability)
        point_durability = 50
        initial_length = 5
        pencil = Pencil(point_durability=point_durability, initial_length=initial_length, eraser=eraser)
        paper = Paper()
        pencil.write(paper, 'test that eraser degrades correct amount')
        pencil.erase(paper, 'eraser')
        self.assertEqual(4, eraser.durability)

    def test_that_eraser_erases_multiple_words_correctly(self):
        durability = 20
        eraser = Eraser(durability=durability)
        point_durability = 100
        initial_length = 5
        pencil = Pencil(point_durability=point_durability, initial_length=initial_length, eraser=eraser)
        paper = Paper()
        input_text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
        pencil.write(paper, input_text)
        pencil.erase(paper, 'chuck')
        pencil.erase(paper, 'chuck')
        expected_text = 'How much wood would a woodchuck chuck if a wood      could       wood?'
        self.assertEqual(expected_text, paper.display_page())


if __name__ == '__main__':
    unittest.main()
