#!/usr/bin/python3
"""The Text indentation """


def text_indentation(text):
    """
    func that prints text with 2 new lines after each '.' '?' or ':'
    Args:
    text: string
    """
    begin = 0
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for a, b in enumerate(text):
        if b in '.?:':
            print(text[begin: a + 1].strip() + '\n')
            begin = a + 1
    if begin < len(text):
        print(text[begin:].strip(), end="")
