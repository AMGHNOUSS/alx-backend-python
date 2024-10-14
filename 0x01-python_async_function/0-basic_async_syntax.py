#!/usr/bin/env python3
""" The basics of async"""

import asyncio
import random


async def wait_random(number=10):
    n = random.uniform(0, number)
    await asyncio.sleep(n)
    return (n)
