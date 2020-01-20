class Paper(object):

    def __init__(self):
        self.page_text = ''

    def display_page(self):
        return self.page_text


class Pencil(object):

    def __init__(self, point_durability=None, initial_length=None):
        self.start_point_durability = point_durability
        self.point_durability = point_durability
        if point_durability is None:
            self.start_point_durability = 0
            self.point_durability = 0

        self.length = initial_length

    def write(self, paper, text):
        new_text_characters = [character for character in text]

        final_page_text = []
        final_page_text.append(self._get_current_page_text(paper))
        print(new_text_characters)
        for character in new_text_characters:
            # self._change_point_durability(character)
            if self.point_durability > 0:
                final_page_text.append(character)
            else:
                final_page_text.append(' ')
            self._change_point_durability(character)
        paper.page_text = ''.join(final_page_text)

    def sharpen(self):
        if self.length > 0:
            self.length -= 1
        else:
            self.length = 0
            raise ValueError('Sorry, the pencil cannot be sharpened anymore because the length is \
                             already zero')
        self.point_durability = self.start_point_durability

    def erase(self, paper, text_to_erase):
        current_page_text = self._get_current_page_text(paper)
        start_index_of_word_to_erase = current_page_text.rfind(text_to_erase)
        first_half_of_text = current_page_text[:start_index_of_word_to_erase]
        second_half_of_text = current_page_text[start_index_of_word_to_erase:]
        spaces_for_text_to_erase = [' ' for character in text_to_erase]
        spaces = ''.join(spaces_for_text_to_erase)
        second_half_of_text = second_half_of_text.replace(text_to_erase, spaces)
        print('{} : {}'.format(first_half_of_text, second_half_of_text))
        new_page_text = first_half_of_text + second_half_of_text
        print('new page text: {}'.format(new_page_text))
        paper.page_text = new_page_text

    def _change_point_durability(self, character):
        ignore_characters = ['\n', ' ']
        if character not in ignore_characters:
            self.point_durability -= 1
        if character.isupper():
            self.point_durability -= 1
        if self.point_durability <= 0:
            self.point_durability = 0

    def _get_current_page_text(self, paper):
        current_page_text = paper.display_page()
        return current_page_text
