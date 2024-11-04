#!/usr/bin/env python3
"""defines the measure_runtime function"""
import time
import asyncio

async_com = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """returns the time to run four comprehension"""
    s = time.perf_counter()
    await asyncio.gather(async_com(), async_com(), async_com(), async_com())
    t = time.perf_counter()
    return (t - s)
