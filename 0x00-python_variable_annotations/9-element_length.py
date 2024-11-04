#!/usr/bin/env python3
"""file that anotate te following function
def element_length(lst):
return [(i, len(i)) for i in lst]
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuple containing iterables and len"""
    return [(i, len(i)) for i in lst]
