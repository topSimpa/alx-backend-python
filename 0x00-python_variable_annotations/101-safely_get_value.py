#!/usr/bin/env python3
"""Given the parameters and the return values,
add type annotations to the function
Hint: look into TypeVar
def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""

from typing import Any, TypeVar, Mapping, Union


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'),
                                    None] = None) -> Union[Any, TypeVar('T')]:
    """safely gets values from dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
