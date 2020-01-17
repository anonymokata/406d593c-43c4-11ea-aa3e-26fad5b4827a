class Paper(object):

    def __init__(self):
        self.page_text = ''

    def display_page(self):
        return self.page_text


class Pencil(object):

    def write(self, paper, text):
        new_page_text = []
        new_page_text.append(paper.page_text)
        new_page_text.append(text)
        paper.page_text = ''.join(new_page_text)
