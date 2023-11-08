""" Profile functions """

import time


# TODO: Make decorator too
def timefunc(f, *args, count=1000):
    accumulate_timings = 0
    for _ in range(count):
        start = time.time()
        f(*args)
        end = time.time()
        accumulate_timings += end - start
    return accumulate_timings / count
