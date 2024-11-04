#!/usr/bin/env python3
"""defines the async_comprehension function"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returns a list of float from async_generator yes"""
    result: List[float] = [i async for i in async_generator()]
    return (result)
