class Paper(object):

    def __init__(self):
        self.page_text = ''

    def display_page(self):
        return self.page_text

class Pencil(object):

    def write(self, paper, text):
        paper.page_text = text
