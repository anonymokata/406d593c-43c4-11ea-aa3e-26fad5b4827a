class Paper(object):

    def __init__(self):
        self._page_text = ''

    def display_page(self):
        return self._page_text

    def add_text(self, text_to_add):
        final_page_text = []
        final_page_text.append(self._page_text)
        final_page_text.extend(text_to_add)
        self._page_text = ''.join(final_page_text)

    def remove_text(self, text_to_remove, num_characters_to_remove=None):
        current_page_text = self._get_current_page_text()
        start_index_of_text_to_remove = current_page_text.rfind(text_to_remove)
        if start_index_of_text_to_remove == -1:
            raise ValueError('Text cannot be removed because it is not present')
        first_half_of_text = current_page_text[:start_index_of_text_to_remove]
        second_half_of_text = current_page_text[start_index_of_text_to_remove:]
        if num_characters_to_remove is None:
            replacement_text = self._replace_all_text_with_spaces(text_to_remove)
        else:
            replacement_text = self._replace_partial_text_with_spaces(text_to_remove,
                                                                      num_characters_to_remove)
        second_half_of_text = second_half_of_text.replace(text_to_remove, replacement_text)
        new_page_text = first_half_of_text + second_half_of_text
        self._page_text = new_page_text

    def _get_current_page_text(self):
        current_page_text = self.display_page()
        return current_page_text

    def _replace_all_text_with_spaces(self, text_to_replace):
        spaces_for_text_to_replace = [' ' for character in text_to_replace]
        spaces = ''.join(spaces_for_text_to_replace)
        return spaces

    def _replace_partial_text_with_spaces(self, text_to_replace, num_characters_to_replace):
        final_text = []
        reversed_text_to_replace = reversed(text_to_replace)
        for i, character in enumerate(reversed_text_to_replace):
            print('i: {}, char: {}'.format(i, character))
            if character not in ['\n', ' '] and num_characters_to_replace > 0:
                final_text.append(' ')
                num_characters_to_replace -= 1
            else:
                final_text.append(character)

        final_text = reversed(final_text)
        final_text = ''.join(final_text)
        return final_text
