#!/usr/bin/env python3
"""file for a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats
and returns their sum as a float."""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """sums a list of float"""
    return float(sum(mxd_list))