"""
---------------------------------------------------------------------
TextNode
M Doyle 13/08/2024
---------------------------------------------------------------------
"""

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text 
        self.text_type = text_type
        self.url = url 

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        
    def __repr__(self):
        return ("TextNode(%s, %s, %s)" % (self.text, self.text_type, self.url))
    

        
    
