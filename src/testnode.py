"""
---------------------------------------------------------------------
test nodes!
M Doyle 13/08/2024
---------------------------------------------------------------------
"""

import unittest

from textnode import TextNode
from html import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("Hello", "bold")
        node2 = TextNode("Hello", "bold")
        self.assertEqual(node, node2)


    def test_print(self):
        node = TextNode("Hello", "bold")
        node2 = TextNode("Hello", "bol")
        print(node)
        print(node2)

        tag = 'p'
        value = 'This is some writing.'
        children = [node, node2]
        props = {"href": "https://www.google.com", "target": "_blank"}

        htmlnode = HTMLNode(tag, value, children, props)
        print(htmlnode)

        print(LeafNode("p", "This is a paragraph of text."))
        print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}))


    def test_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        node.to_html()

if __name__ == "__main__":
    unittest.main()