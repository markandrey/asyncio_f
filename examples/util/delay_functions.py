import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'sleep on {delay_seconds} s.')
    await asyncio.sleep(delay_seconds)
    print(f'sleeping on {delay_seconds} s. end')
    return delay_seconds
