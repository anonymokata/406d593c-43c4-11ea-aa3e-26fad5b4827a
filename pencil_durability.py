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
        new_text_characters = [character for character in text]

        final_page_text = []
        final_page_text.append(self._get_current_page_text(paper))
        print(new_text_characters)
        for character in new_text_characters:
            self._change_point_durability(character)
            if self.point_durability >= 0:
                final_page_text.append(character)
            else:
                final_page_text.append(' ')
        paper.page_text = ''.join(final_page_text)

    def _change_point_durability(self, character):
        ignore_characters = ['\n', ' ']
        if character not in ignore_characters:
            self.point_durability -= 1
        if character.isupper():
            self.point_durability -= 1

    def _get_current_page_text(self, paper):
        current_page_text = paper.display_page()
        return current_page_text
