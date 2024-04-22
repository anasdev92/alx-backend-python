#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('0-basic_async_syntax').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
