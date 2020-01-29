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
        #new_text_characters = [character for character in text]
        new_text = []

        for character in text:
            if self.point_durability > 0:
                new_text.append(character)
            else:
                new_text.append(' ')
            self._change_point_durability(character)

        paper.add_text(new_text)

    def sharpen(self):
        if self.length > 0:
            self.length -= 1
        else:
            self.length = 0
            raise ValueError('Sorry, the pencil cannot be sharpened anymore because the length is \
                             already zero')
        self.point_durability = self.start_point_durability

    def erase(self, paper, text_to_erase):
        self.eraser.erase(paper, text_to_erase)

    def edit(self, paper, replacement_text, method=None, erase_number=None, location_index=None):
        new_text_characters = [character for character in replacement_text]
        new_text = []

        for character in new_text_characters:
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
