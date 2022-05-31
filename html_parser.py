class Tag(object):

    def __init__(self, tagtype=None, attributes=None, html=None):
        self.tagtype = tagtype
        self.attributes = attributes
        self.html = html

    def get_attribute(self, name):
        try:
            return self.attributes[name]
        except KeyError as error:
            print(error)
            return None
    
    def get_innerHTML(self):
        return self.html

class DOMTreeNode(object):
    
    def __init__(self, content, children):
        self.content = content
        self.children = children

    def get_child(self, nth):
        try:
            return self.children[nth]
        except IndexError as e:
            print(e)
            return None

    def get_child_of_type(self, tagtype=None):
        for child in self.children:
            if child.content.tagtype == tagtype:
                return child

    def get_children_of_type(self, tagtype=None):
        results = []
        for child in self.children:
            if child.content.tagtype == tagtype:
                result.append(child)

        return results


class Token(object):

    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value


class Lexer(object):

    def __init__(self, text):
        self.text = text
        self.cursor = 0
        self.length = len(text)

    def next(self):
        if self.cursor >= self.length:
            return '\0'
        else:
            ret = self.text[self.cursor]
            self.cursor += 1
            return ret

    def prev(self):
        if self.cursor <= 0:
            return '\0'
        else:
            self.cursor -= 1
            return self.text[self.cursor]

    def seek(self, pos):
        if pos >= 0 and pos < self.length:
            self.cursor = pos
            return self.text[self.cursor]
        else:
            return '\0'

    def is_eof(self):
        return self.cursor >= self.pos

    def lex(self):
        tokens = []
        string_context = False
        tag_context = False
        inner_html_context = False
        token_stack = ""
        while not self.is_eof():
            scanned = self.next()
            match scanned:
                case '"':
                    if string_context:
                        tokens.append(Token("string", token_stack))
                        token_stack = ""
                        string_context = False
                    else:
                        if len(token_stack) > 0:
                            tokens.append(Token('token', token_stack))
                            token_stack = ""
                        string_context = True
                case ' ' | '\t' | '\n':
                    if string_context:
                        token_stack += scanned
                    else:
                        if len(token_stack) > 0:
                            tokens.append(Token("token", token_stack))
                            token_stack = ""

        return tokens

class HTMLParser(object):

    def __init__(self):
        self.raw = ''
    

