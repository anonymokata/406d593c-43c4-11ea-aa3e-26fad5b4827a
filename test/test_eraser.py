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

    def test_that_eraser_erases_multiple_words_at_one_time_correctly(self):
        self.pencil.write(self.paper, 'test that eraser degrades correct amount')
        self.pencil.erase(self.paper, 'test that')
        expected_text = '          eraser degrades correct amount'
        self.assertEqual(expected_text, self.paper.display_page())

    def test_that_eraser_erases_multiple_words_one_after_another_correctly(self):
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

    def test_that_eraser_raises_value_error_if_text_to_erase_is_not_present(self):
        input_text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
        paper = Paper(input_text)
        with self.assertRaises(ValueError):
            self.pencil.erase(paper, 'how')

    def test_that_eraser_does_not_erase_when_it_is_given_an_empty_string(self):
        input_text = 'How much wood...'
        paper = Paper(input_text)
        self.pencil.erase(paper, '')
        self.assertEqual('How much wood...', paper.display_page())


if __name__ == '__main__':
    unittest.main()
