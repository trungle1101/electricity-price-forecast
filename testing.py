import time
import functools32

@functools32.lru_cache(maxsize=32)
def slow_function(input):
    time.sleep(5)
    return 'Input was {}'.format(input)

print(slow_function(2))
print(slow_function(2))