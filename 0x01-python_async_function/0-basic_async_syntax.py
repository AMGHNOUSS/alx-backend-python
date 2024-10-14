#!/usr/bin/env python3
""" """

import asyncio
import random

async def wait_random(number=10):
    n = random.randint(0, number)
    await asyncio.sleep(n)
    return (n)
