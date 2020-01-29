from Eraser import Eraser


class Pencil(object):

    def __init__(self, point_durability=None, initial_length=None, eraser=None):
        self.start_point_durability = point_durability
        self.point_durability = point_durability
        if point_durability is None:
            self.start_point_durability = 0
            self.point_durability = 0

        self.length = initial_length
        if eraser is None:
            self.eraser = Eraser()
        else:
            self.eraser = eraser

    def write(self, paper, text):
        '''
        Function to write text to a piece of paper

        Args:
            paper (Paper): A piece of paper
            text (str): text that the pencil is supposed to write

        Returns:
            None
        '''
        new_text = []

        for character in text:
            if self.point_durability > 0:
                new_text.append(character)
            else:
                new_text.append(' ')
            self._change_point_durability(character)

        paper.add_text(new_text)

    def sharpen(self):
        '''
        Function to sharpen pencil, reducing point durability by 1 for each non-whitespace character

        Returns:
            None

        Raises:
            ValueError: raises error when we try to erase a pencil that has length 0
        '''
        if self.length > 0:
            self.length -= 1
        else:
            self.length = 0
            raise ValueError('Sorry, the pencil cannot be sharpened anymore because the length is \
                             already zero')
        self.point_durability = self.start_point_durability

    def erase(self, paper, text_to_erase):
        '''
        Function to erase text from a piece of paper

        Args:
            text_to_erase (str): text that we want the pencil to erase

        Returns:
            None
        '''
        self.eraser.erase(paper, text_to_erase)

    def edit(self, paper, replacement_text, method='index', erase_number=None, location_index=0):
        '''
        Function to edit a piece of paper based on either an index or the location of erasure

        Args:
            paper (Paper): piece of paper
            replacement_text (str): the text to be edited into the document
            method (Optional[str]): Either 'index' or 'erase' depending on whether text should be
                edited based on a given index or based on the order by which erasing took place.
                Defaults to None.
            erase_number (Optional[int]): Represemts when in order some text was erased, so 1
                corresponds to the first text that was erased, 2 to the second, and so on. Defaults
                to None.
            location_index (Optional[int]): Represents the index location of where to begin editing.
                Defaults to 0 so we begin editing at the start of the paper if nothing is passed in

        Returns:
            None
        '''
        new_text = []

        for character in replacement_text:
            if self.point_durability > 0:
                new_text.append(character)
            else:
                new_text.append(' ')
            self._change_point_durability(character)

        if method == 'index':
            paper.replace_text_by_index(new_text, location_index)
        elif method == 'erase':
            paper.replace_text_by_erase_order(new_text, erase_number)

    def _change_point_durability(self, character):
        ignore_characters = ['\n', ' ']
        if character not in ignore_characters:
            self.point_durability -= 1
        if character.isupper():
            self.point_durability -= 1
        if self.point_durability <= 0:
            self.point_durability = 0
