#!/usr/bin/python3

"""
Module that provides a function to convert a JSON string to a Python object.
"""
import json as j


def from_json_string(my_str):
    """
    Return the Python object represented by a JSON string.
    """
    return j.loads(my_str)
