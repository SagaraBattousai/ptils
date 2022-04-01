import time

__all__ = ['timefunc']

def timefunc(f, *args, count=1000):
  sum = 0
  for _ in range(count):
    start = time.time()
    f(*args)
    end = time.time()
    sum += (end - start)
  return sum / count
