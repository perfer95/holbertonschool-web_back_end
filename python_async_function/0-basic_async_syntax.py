#!/usr/bin/env python3
"""
0. The basics of async
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait up to max_delay seconds and then return length of delay.
    """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time

asyncio.run(wait_random())
