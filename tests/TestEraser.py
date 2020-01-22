import unittest
from Eraser import Eraser
from Paper import Paper
from Pencil import Pencil


class TestEraser(unittest.TestCase):
    def setUp(self):
        durability = 10
        self.eraser = Eraser(durability=durability)
        point_durability = 100
        initial_length = 5
        self.pencil = Pencil(point_durability=point_durability, initial_length=initial_length, eraser=self.eraser)
        self.paper = Paper()

    def test_that_eraser_erases_last_occurance_of_text_on_paper(self):
        self.pencil.write(self.paper, 'test the eraser test the eraser')
        self.pencil.erase(self.paper, 'eraser')
        self.assertEqual('test the eraser test the       ', self.paper.display_page())

    def test_that_eraser_can_be_initialized_with_a_durability(self):
        durability = 10
        eraser = Eraser(durability=durability)
        self.assertEqual(10, eraser.durability)

    def test_that_eraser_degrades_correct_amount_for_non_whitespace_characters(self):
        self.pencil.write(self.paper, 'test that eraser degrades correct amount')
        self.pencil.erase(self.paper, 'eraser')
        self.assertEqual(4, self.eraser.durability)

    def test_that_eraser_degrades_correct_amount_for_whitespace_characters(self):
        self.pencil.write(self.paper, 'test that eraser degrades correct amount')
        self.pencil.erase(self.paper, 'test that')
        self.assertEqual(2, self.eraser.durability)

    def test_that_eraser_erases_multiple_words_correctly(self):
        input_text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
        self.pencil.write(self.paper, input_text)
        self.pencil.erase(self.paper, 'chuck')
        self.pencil.erase(self.paper, 'chuck')
        expected_text = 'How much wood would a woodchuck chuck if a wood      could       wood?'
        self.assertEqual(expected_text, self.paper.display_page())

    def test_that_eraser_erases_word_in_opposite_order(self):
        durability = 3
        eraser = Eraser(durability=durability)
        point_durability = 100
        initial_length = 5
        pencil = Pencil(point_durability=point_durability, initial_length=initial_length, eraser=eraser)
        paper = Paper()
        pencil.write(paper, 'Buffalo Bill')
        pencil.erase(paper, 'Bill')
        self.assertEqual('Buffalo B   ', paper.display_page())


if __name__ == '__main__':
    unittest.main()
