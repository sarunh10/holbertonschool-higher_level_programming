#!/usr/bin/python3

"""
Module that provides a helper function to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF-8)
    and return the number of characters added.
    """

    with open(filename, "a", encoding="UTF8") as f:
        return f.write(text)
