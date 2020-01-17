import unittest
from pencil_durability import Paper, Pencil

class TestPencil(unittest.TestCase):

    def test_that_pencil_writes_on_paper(self):
        paper = Paper()
        pencil = Pencil()
        pencil.write(paper, 'She sells sea shells')
        self.assertEqual('She sells sea shells', paper.display_page())


if __name__ == '__main__':
    unittest.main()
