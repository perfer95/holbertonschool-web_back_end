#!/usr/bin/env python3
"""
2. Measure the runtime
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_random


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return float(total_time / n)

if __name__ = "__main__":
    measure_time(2, 10)
