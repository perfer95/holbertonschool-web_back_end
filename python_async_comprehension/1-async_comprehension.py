#!/usr/bin/env python3
"""
1. Async Comprehensions
"""

import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehensing over
    async_generator, then return the 10 random numbers.
    """
    return [numbers async for numbers in async_generator()]

if __name__ == "__main__":
    asyncio.run(async_comprehension())
