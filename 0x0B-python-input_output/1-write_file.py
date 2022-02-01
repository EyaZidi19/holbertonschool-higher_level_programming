#!/usr/bin/python3
""" function to Write a file """


def write_file(filename="", text=""):
    """
        Write a string to a text file (UTF8)
        and return the number of characters
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
    print(len(text))
