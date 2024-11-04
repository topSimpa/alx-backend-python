#!/usr/bin/env python3
"""defines the coruotine wait_n"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """takes two arguments n, maxdelay, and
    calls wait_random n types with max_delay
    then returns of delays in ascending order."""

    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))

    asc_times = []
    for coroutine in asyncio.as_completed(tasks):
        asc_times.append(await coroutine)

    return asc_times
