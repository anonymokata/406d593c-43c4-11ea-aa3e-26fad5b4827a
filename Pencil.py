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
        new_text_characters = [character for character in text]
        new_text = []

        for character in new_text_characters:
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

    def _change_point_durability(self, character):
        ignore_characters = ['\n', ' ']
        if character not in ignore_characters:
            self.point_durability -= 1
        if character.isupper():
            self.point_durability -= 1
        if self.point_durability <= 0:
            self.point_durability = 0
