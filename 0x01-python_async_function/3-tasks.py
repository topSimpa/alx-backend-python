#!/usr/bin/env python3
"""defines task_wait_random function"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return a task object for wait_random"""
    return (asyncio.Task(wait_random(max_delay)))
