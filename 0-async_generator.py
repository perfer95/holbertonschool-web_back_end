#!/usr/bin/env python3
"""
0. Async Generator
"""
import asyncio
import random
import typing


async def async_generator() -> Generator[float]:
    """
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for i in range(10):
        await sleep(1)
        yield random.uniform(0, 10)
