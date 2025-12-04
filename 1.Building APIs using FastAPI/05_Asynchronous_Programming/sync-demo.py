""" 
    We have 3 tasks, T1, T2, and T3. Each task takes a different amount of time to complete:
    - T1 takes 2 seconds
    - T2 takes 1 seconds
    - T3 takes 3 seconds
    We want to run these tasks sequentially and measure the total time taken to complete all tasks.
"""
import time
from timeit import default_timer as timer

def run_task(name, seconds):
    print(f'{name} started at: {timer()}')
    time.sleep(seconds)
    print(f'{name} completed at: {timer()}')

start = timer()
run_task('T1', 2)
run_task('T2', 1)
run_task('T3', 3)
print(f'\nTotal time taken: {(timer() - start):.2f} seconds')
