#!/usr/bin/env python3
"""
2. Basic annotations - floor
"""


def floor(n: float) -> int:
    """
    Takes a float n as argument and returns the floor of the float
    """
    if n >= 0:
        return int(n)
    return int(n) - 1
