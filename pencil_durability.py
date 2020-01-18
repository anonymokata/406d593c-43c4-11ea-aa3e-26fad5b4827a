class Paper(object):

    def __init__(self):
        self.page_text = ''

    def display_page(self):
        return self.page_text


class Pencil(object):

    def __init__(self, point_durability=None):
        self.point_durability = point_durability
        if point_durability is None:
            self.point_durability = 0

    def write(self, paper, text):
        new_page_text = []
        new_page_text.append(paper.page_text)
        new_page_text.append(text)
        new_page_text = [list(text) for text in new_page_text]
        new_page_text_characters = [character for sublist in new_page_text for character in sublist]

        final_page_text = []
        print(new_page_text_characters)
        for character in new_page_text_characters:
            self._change_point_durability(character)
        paper.page_text = ''.join(new_page_text_characters)

    def _change_point_durability(self, character):
        if character.islower():
            self.point_durability -= 1
        elif character.isupper():
            self.point_durability -= 2
