#!/usr/bin/env python3
""""defines the async_generator function"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """yields a random number ten times"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
