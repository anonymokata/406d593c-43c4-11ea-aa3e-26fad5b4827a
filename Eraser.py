class Eraser(object):

    def __init__(self):
        pass

    def erase(self, paper, text_to_erase):
        current_page_text = self._get_current_page_text(paper)
        start_index_of_word_to_erase = current_page_text.rfind(text_to_erase)
        first_half_of_text = current_page_text[:start_index_of_word_to_erase]
        second_half_of_text = current_page_text[start_index_of_word_to_erase:]
        spaces_for_text_to_erase = [' ' for character in text_to_erase]
        spaces = ''.join(spaces_for_text_to_erase)
        second_half_of_text = second_half_of_text.replace(text_to_erase, spaces)
        new_page_text = first_half_of_text + second_half_of_text
        paper.page_text = new_page_text
