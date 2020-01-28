class Eraser(object):

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
        whitespace_characters = {'\n', ' '}
        if character not in whitespace_characters:
            self.durability -= 1

    def _count_non_whitespace_characters(self, text):
        return len(text) - text.count(' ') - text.count('\n')
