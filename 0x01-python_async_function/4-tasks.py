#!/usr/bin/env python3
"""defines the task_wait_n function"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """"an async routine that n task_wait_random time"""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    n_list = []

    for coro in asyncio.as_completed(tasks):
        n_list.append(await coro)

    return n_list
