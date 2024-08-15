#!/usr/bin/env python3
"""
5. Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list input_list of floats as argument and
    returns their sum as a float.
    """
    a = 0.0
    for i in range(len(input_list)):
        a += input_list[i]
    return a
