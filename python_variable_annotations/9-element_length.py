#!/usr/bin/env python3
"""
9. Let's duck type an iterable object
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Take an iterable and return a list of tuples
    """
    return [(i, len(i)) for i in lst]
