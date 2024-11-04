#!/usr/bin/env python3
"""file for a type-annotated function floor
which takes a float n as argument and
returns the floor of the float.
"""


def floor(n: float) -> int:
    """takes a float to the nearest smallest integer"""
    if n < 0:
        return (int(n) - 1)
    return(int(n))
