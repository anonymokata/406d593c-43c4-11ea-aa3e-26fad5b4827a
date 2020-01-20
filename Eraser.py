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
        paper.remove_text(text_to_erase)
