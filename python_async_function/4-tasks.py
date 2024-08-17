#!/usr/bin/env python3
"""
4. Tasks
"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return the list of all the delays (float values)
    in ascending order.
    """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    results = []

    for task in asyncio.as_completed(tasks):
        delay_time = await task
        results.append(delay_time)

    return results

if __name__ == "__main__":
    asyncio.run(wait_n)
