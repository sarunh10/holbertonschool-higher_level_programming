#!/usr/bin/python3
"""
This module defines an function that returns the list of available attributes
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
