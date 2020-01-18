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


if __name__ == '__main__':
    unittest.main()
