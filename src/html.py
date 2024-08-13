"""
---------------------------------------------------------------------
HTMLNodes (tree structure)
M Doyle 13/08/2024
---------------------------------------------------------------------
"""

from textnode import TextNode

class HTMLNode:
    def __init__(self, 
                 tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        NotImplementedError
    
    def props_to_html(self):
        str = ""
        for key, value in self.props.items():
            str += key + '="' +value + '" '
        return str

    def __repr__(self):
        return ("HTMLNode(%s, %s, %s, %s)" % (self.tag, 
                                              self.value, 
                                              str(self.children), 
                                              self.props_to_html()))
    
class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag = tag, value = value, props = props)
        if self.value is None:
            print("Value can not be None under a leaf node.")
            ValueError
        if self.tag == None:
            self.tag = ""

    def props_to_html(self):
        str = ""
        for key, value in self.props.items():
            str += key + '="' +value + '" '
        return str
    
    def to_html(self):
        if self.props is None:
            tag_open = "<" + self.tag + ">"
            tag_close = "</" + self.tag + ">"
            if self.tag == "":
                tag_open = ""
                tag_close = ""
            return tag_open + self.value + tag_close
        else:
            return "<" + self.tag + " " + self.props_to_html()[:-1] + ">" + self.value + "</" + self.tag + ">"

    def __repr__(self):
        return self.to_html()


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag = tag, children = children, props = props)
        

    def to_html(self):
        if self.children is None:
            print("Children can not be None under a parent node.")
            ValueError
        if self.tag is None:
            print("Tag can not be None under a parent node.")
            ValueError

        str = "<" + self.tag + ">"
        for child in self.children:
            str += child.to_html() 
        str += "</" + self.tag + ">"
        print(str)
        return str


def text_node_to_html_node(text_node):
    """
    It should handle each type of TextNode:

    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"
    If it gets a TextNode that is none of those types, it should raise an exception.

    text_type_text: This should become a LeafNode with no tag, just a raw text value.
    text_type_bold: This should become a LeafNode with a "b" tag and the text
    text_type_italic: "i" tag, text
    text_type_code: "code" tag, text
    text_type_link: "a" tag, anchor text, and "href" prop
    text_type_image: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
    """