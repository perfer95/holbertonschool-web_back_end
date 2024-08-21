#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
"""

import time
import asyncio
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime and return it
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                        async_comprehension(), async_comprehension())
    end_time = time.time()

    return end_time - start_time
