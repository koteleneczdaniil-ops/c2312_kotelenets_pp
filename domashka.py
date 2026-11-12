import time


def measure_time(func, *args, **kwargs):
  start = time.time()
  result = func(*args, **kwargs)
  end = time.time()
  print(f"Функція працювала: {end - start:} сек.")
  return result

def example_func(n):
  return sum(range(n))

measure_time(example_func, 1000000)