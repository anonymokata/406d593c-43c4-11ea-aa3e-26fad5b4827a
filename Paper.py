class Paper(object):
    WHITESPACE_CHARS = ['\n', ' ']

    def __init__(self, original_text=None):
        if original_text is None:
            self._page_text = ''
        else:
            self._page_text = original_text
        self._number_of_times_text_removed = 0
        self._removed_text_locations = {}

    def display_page(self):
        return self._page_text

    def add_text(self, text_to_add):
        final_page_text = []
        final_page_text.append(self._page_text)
        final_page_text.extend(text_to_add)
        self._page_text = ''.join(final_page_text)

    def remove_text(self, text_to_remove, num_characters_to_remove=None):
        current_page_text = self.display_page()
        start_index_of_text_to_remove = self._find_text(text_to_remove)
        if start_index_of_text_to_remove == -1:
            raise ValueError('Text cannot be removed because it is not present')

        first_half = current_page_text[:start_index_of_text_to_remove]
        second_half = current_page_text[start_index_of_text_to_remove:]

        if num_characters_to_remove is None:
            replacement_text = self._replace_all_text_with_spaces(text_to_remove)
        else:
            replacement_text = self._replace_partial_text_with_spaces(text_to_remove,
                                                                      num_characters_to_remove)

        second_half = second_half.replace(text_to_remove, replacement_text)
        new_page_text = first_half + second_half
        self._text_removed(start_index_of_text_to_remove)
        self._page_text = new_page_text

    def replace_text_by_index(self, replacement_text, location_index):
        current_page_text = self._get_current_page_text()
        first_half = current_page_text[:location_index]
        second_half = list(current_page_text[location_index:])

        if len(second_half) < len(replacement_text):
            second_half = self._create_replacement_text_for_paper_overflow(replacement_text,
                                                                           second_half)
        else:
            second_half = self._create_replacement_text(replacement_text, second_half)
        second_half = ''.join(second_half)
        new_page_text = first_half + second_half
        self._page_text = new_page_text

    def replace_text_by_erase_order(self, replacement_text, erase_number):
        location_index = self._removed_text_locations.get(erase_number)
        if location_index is not None:
            self.replace_text_by_index(replacement_text, location_index)

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
            if character not in ['\n', ' '] and num_characters_to_replace > 0:
                final_text.append(' ')
                num_characters_to_replace -= 1
            else:
                final_text.append(character)

        final_text = reversed(final_text)
        final_text = ''.join(final_text)
        return final_text

    def _find_text(self, text_to_find):
        current_page_text = self._get_current_page_text()
        return current_page_text.rfind(text_to_find)

    def _text_removed(self, location):
        self._number_of_times_text_removed += 1
        num = self._number_of_times_text_removed
        self._removed_text_locations[num] = location

    def _create_replacement_text_for_paper_overflow(self, replacement_text, end_text):
        inside_of_document = True
        i = 0
        while inside_of_document:
            if replacement_text[i] not in self.WHITESPACE_CHARS \
                    and end_text[i] not in self.WHITESPACE_CHARS:
                end_text[i] = '@'
            else:
                end_text[i] = replacement_text[i]
            i += 1
            if i >= len(end_text):
                inside_of_document = False
        while i < len(replacement_text):
            end_text.append(replacement_text[i])
            i += 1

        return end_text

    def _create_replacement_text(self, replacement_text, end_text):
        for i, character in enumerate(replacement_text):
            if character not in self.WHITESPACE_CHARS and end_text[i] not in self.WHITESPACE_CHARS:
                end_text[i] = '@'
            else:
                end_text[i] = character

        return end_text
