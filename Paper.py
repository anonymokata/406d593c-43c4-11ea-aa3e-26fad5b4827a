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

    def remove_text(self, text_to_remove):
        current_page_text = self._get_current_page_text()
        start_index_of_word_to_erase = current_page_text.rfind(text_to_remove)
        first_half_of_text = current_page_text[:start_index_of_word_to_erase]
        second_half_of_text = current_page_text[start_index_of_word_to_erase:]
        spaces_for_text_to_erase = [' ' for character in text_to_remove]
        spaces = ''.join(spaces_for_text_to_erase)
        second_half_of_text = second_half_of_text.replace(text_to_remove, spaces)
        new_page_text = first_half_of_text + second_half_of_text
        self._page_text = new_page_text

    def _get_current_page_text(self):
        current_page_text = self.display_page()
        return current_page_text
