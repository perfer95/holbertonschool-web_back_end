#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return the list of all the delays (float values)
    in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    results = []

    for task in asyncio.as_completed(tasks):
        delay_time = await task
        results.append(delay_time)

    return results

if __name__ == "__main__":
    asyncio.run(wait_n)
