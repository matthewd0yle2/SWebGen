# -*- coding: utf-8 -*-
from textnode import TextNode


TEXT = 'Hello'
TEXT_TYPE = 'Greeting'
URL = 'www.google.com'

def main():
    A = TextNode(TEXT, TEXT_TYPE)
    out = A.__repr__()
    print(out)

if __name__:
    main()