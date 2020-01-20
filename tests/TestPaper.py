import unittest
from Paper import Paper


class TestPaper(unittest.TestCase):
    def test_that_initializing_blank_paper_is_blank_paper(self):
        paper = Paper()
        self.assertEqual('', paper.display_page())


if __name__ == '__main__':
    unittest.main()
