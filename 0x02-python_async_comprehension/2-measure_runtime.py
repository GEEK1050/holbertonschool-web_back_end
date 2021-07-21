#!/usr/bin/env python3
"""2-measure_runtime"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    measure_runtime: a coroutine that execute async_comprehension
    4 times and mesure the runtime
    """
    beg = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    runtime = time.time() - beg
    return runtime
