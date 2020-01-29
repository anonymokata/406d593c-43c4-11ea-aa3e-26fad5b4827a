class Eraser(object):
    WHITESPACE_CHARS = {' ', '\n'}

    def __init__(self, durability=10):
        self.durability = durability

    @property
    def durability(self):
        return self._durability

    @durability.setter
    def durability(self, value):
        if value <= 0:
            self._durability = 0
        else:
            self._durability = value

    def erase(self, paper, text_to_erase):
        '''
        Function to erase text from a piece of paper

        Args:
            paper (Paper): A piece of paper
            text_to_erase (str): text that the eraser should erase

        Returns:
            None
        '''
        count_characters_that_degrade_eraser = self._count_non_whitespace_characters(text_to_erase)
        if self.durability < count_characters_that_degrade_eraser:
            count_characters_to_remove = self.durability
        else:
            count_characters_to_remove = 0
        for character in text_to_erase:
            self._degrade_eraser(character)

        if count_characters_to_remove > 0:
            paper.remove_text(text_to_erase, count_characters_to_remove)
        else:
            paper.remove_text(text_to_erase)

    def _degrade_eraser(self, character):
        '''
        Function to degrade eraser by correct amount according to character being erased

        Args:
            character (str): a character to be erased

        Returns:
            None
        '''
        if character not in self.WHITESPACE_CHARS:
            self.durability -= 1

    def _count_non_whitespace_characters(self, text):
        '''
        Function to get the count of non-whitespace characters in text

        Args:
            text (str): text to analyze

        Returns:
            The count of non-whitespace characters in the passed in text
        '''
        count_non_whitespace_chars = len(text)
        for whitespace_char in self.WHITESPACE_CHARS:
            count_non_whitespace_chars -= text.count(whitespace_char)
        return count_non_whitespace_chars
