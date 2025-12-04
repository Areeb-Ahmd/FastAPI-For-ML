""" 
    We have 3 tasks, T1, T2, and T3. Each task takes a different amount of time to complete:
    - T1 takes 2 seconds
    - T2 takes 1 seconds
    - T3 takes 3 seconds
    we want to run these tasks asequentially and measure the total time taken to complete all tasks.
"""

import asyncio
from timeit import default_timer as timer

async def run_task(name, seconds):
    print(f'{name} started at: {timer()}')
    await asyncio.sleep(seconds)
    print(f'{name} completed at: {timer()}')

async def main():
    start = timer()
    await asyncio.gather(
        run_task('T1', 2),
        run_task('T2', 1),
        run_task('T3', 3)
    )
    print(f'\nTotal time taken: {(timer() - start):.2f} seconds')

asyncio.run(main())