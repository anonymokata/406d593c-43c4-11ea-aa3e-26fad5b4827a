import unittest
from Paper import Paper


class TestPaper(unittest.TestCase):
    def test_that_initializing_blank_paper_is_blank_paper(self):
        paper = Paper()
        self.assertEqual('', paper.display_page())

    def test_that_paper_can_be_initialized_with_text(self):
        paper = Paper('This is the original text of the paper')
        self.assertEqual('This is the original text of the paper', paper.display_page())


if __name__ == '__main__':
    unittest.main()
