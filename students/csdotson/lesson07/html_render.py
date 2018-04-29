class Element:
    """Create an Element class for rendering an html element"""
    tag_name = "html"
    indentation = ""

    def __init__(self, content=None):
        self.content = [content] if content else []

    def append(self, content_to_add):
        if isinstance(content_to_add, str):
            self.content.append(TextWrapper(content_to_add))
        else:
            self.content.append(content_to_add)

    def render(self, file_out="f", cur_ind=""):
        print("<"+self.tag_name+">")
        for elem in self.content:
            if isinstance(elem, str):
                elem = TextWrapper(elem)
            elem.render()
        print("</"+self.tag_name+">")
        # file_out.write(output)
        # print(output)


class Html(Element):
    tag_name = 'html'


class Head(Element):
    tag_name = 'head'


class Body(Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'


class OneLineTag(Element):
    def render(self, file_out="f", cur_ind=""):
        open_tag = "<"+self.tag_name+">"
        close_tag = "</"+self.tag_name+">"
        print(open_tag, self.content[0], close_tag)


class Title(OneLineTag):
    tag_name = 'title'


class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out="f", cur_ind=""):
        print(self.text)
        # file_out.write(cur_ind)
        # file_out.write(self.text)
