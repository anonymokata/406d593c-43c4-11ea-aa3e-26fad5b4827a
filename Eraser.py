class Eraser(object):

    def __init__(self):
        pass

    def erase(self, paper, text_to_erase):
        paper.remove_text(text_to_erase)
