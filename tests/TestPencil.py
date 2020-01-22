import unittest
from Paper import Paper
from Pencil import Pencil


class TestPencil(unittest.TestCase):

    def setUp(self):
        self.paper = Paper()
        point_durability = 50
        self.pencil = Pencil(point_durability=point_durability)
        self.pencil.write(self.paper, 'She sells sea shells')
        self.assertEqual('She sells sea shells', self.paper.display_page())

    def test_that_pencil_writes_on_paper(self):
        paper = Paper()
        point_durability = 50
        pencil = Pencil(point_durability=point_durability)
        pencil.write(paper, 'She sells sea shells')
        self.assertEqual('She sells sea shells', paper.display_page())

    def test_that_pencil_writes_where_it_left_off(self):
        paper = Paper()
        point_durability = 50
        pencil = Pencil(point_durability=point_durability)
        pencil.write(paper, 'She sells sea shells')
        pencil.write(paper, ' down by the sea shore')
        self.assertEqual('She sells sea shells down by the sea shore', paper.display_page())

    def test_that_point_durability_can_be_set_on_construction(self):
        point_durability = 10
        pencil = Pencil(point_durability=point_durability)
        self.assertEqual(point_durability, pencil.point_durability)

    def test_that_pencil_not_dull_when_lower_case_text_len_is_less_than_point_durability(self):
        point_durability = 10
        pencil = Pencil(point_durability=point_durability)
        paper = Paper()
        pencil.write(paper, 'test')
        self.assertEqual(6, pencil.point_durability)

    def test_that_pencil_not_dull_when_upper_case_text_should_not_use_up_point_durability(self):
        point_durability = 10
        pencil = Pencil(point_durability=point_durability)
        paper = Paper()
        pencil.write(paper, 'TEST')
        self.assertEqual(2, pencil.point_durability)

    def test_that_pencil_point_durability_does_not_change_for_spaces(self):
        point_durability = 10
        pencil = Pencil(point_durability=point_durability)
        paper = Paper()
        pencil.write(paper, 'test    ')  # 4 spaces written to paper
        self.assertEqual(6, pencil.point_durability)

    def test_that_pencil_point_durability_does_not_change_for_newline_characters(self):
        point_durability = 10
        pencil = Pencil(point_durability=point_durability)
        paper = Paper()
        pencil.write(paper, '\ntest\ntest\n\n\n')  # 4 newlines written to paper
        self.assertEqual(2, pencil.point_durability)

    def test_that_pencil_point_durability_decrements_by_one_for_special_characters(self):
        point_durability = 30
        pencil = Pencil(point_durability=point_durability)
        paper = Paper()
        pencil.write(paper, '~!@#$%^&*()_+`-=:",./<>?{}[]|')  # 29 special chars written to paper
        self.assertEqual(1, pencil.point_durability)

    def test_that_pencil_that_starts_dull_only_writes_empty_spaces(self):
        point_durability = 0
        pencil = Pencil(point_durability=point_durability)
        paper = Paper()
        pencil.write(paper, 'test')
        self.assertEqual('    ', paper.display_page())  # paper should contain 4 spaces

    def test_that_pencil_that_becomes_dull_during_writing_writes_empty_spaces(self):
        point_durability = 4
        pencil = Pencil(point_durability=point_durability)
        paper = Paper()
        pencil.write(paper, 'Test')
        self.assertEqual('Tes ', paper.display_page())  # paper should contain one space at end

    def test_that_pencil_that_becomes_dull_returns_to_start_point_durability_when_sharpened(self):
        point_durability = 15
        initial_length = 5
        pencil = Pencil(point_durability=point_durability, initial_length=initial_length)
        paper = Paper()
        pencil.write(paper, 'Test sharpening')
        self.assertEqual(0, pencil.point_durability)
        pencil.sharpen()
        self.assertEqual(15, pencil.point_durability)

    def test_that_pencil_that_becomes_dull_picks_up_after_spaces_when_sharpened(self):
        point_durability = 5
        initial_length = 5
        pencil = Pencil(point_durability=point_durability, initial_length=initial_length)
        paper = Paper()
        pencil.write(paper, 'Test sharpening')
        self.assertEqual(0, pencil.point_durability)
        pencil.sharpen()
        pencil.write(paper, 'Test sharpening')
        self.assertEqual('Test           Test           ', paper.display_page())

    def test_that_creation_of_pencil_with_initial_length_creates_pencil_with_correct_length(self):
        initial_length = 5
        pencil = Pencil(initial_length=initial_length)
        self.assertEqual(5, pencil.length)

    def test_that_sharpening_pencil_reduces_length_by_one(self):
        initial_length = 5
        pencil = Pencil(initial_length=initial_length)
        pencil.sharpen()
        self.assertEqual(4, pencil.length)

    def test_that_trying_to_sharpen_zero_length_pencil_raises_error(self):
        initial_length = 0
        pencil = Pencil(initial_length=initial_length)
        with self.assertRaises(ValueError):
            pencil.sharpen()

    def test_that_pencil_that_is_sharpened_before_going_dull_continues_to_write(self):
        point_durability = 20
        initial_length = 5
        pencil = Pencil(point_durability=point_durability, initial_length=initial_length)
        paper = Paper()
        pencil.write(paper, 'Testing sharpening.')
        pencil.sharpen()
        pencil.write(paper, ' Testing sharpening.')
        self.assertEqual('Testing sharpening. Testing sharpening.', paper.display_page())


if __name__ == '__main__':
    unittest.main()
