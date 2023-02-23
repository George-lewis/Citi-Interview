# simulate coin flips

from random import random
from time import time
from math import comb

ITERATIONS = 10000000

ph = 0.52
pt = 1 - ph

actual = comb(10, 5) * (ph**5) * (pt**5)

success = 0

start = time()
for _ in range(ITERATIONS):
  num_heads = 0
  for i in range(10):
    if random() < ph:
      num_heads += 1

  if num_heads == 5:
    success += 1
elapsed = time() - start
print(f"naive computation took {elapsed:.3} seconds")

print(success / ITERATIONS)
print(actual)

import numpy as np

start = time()
observations = np.sum(np.sum(np.random.random((10, ITERATIONS)) < ph, axis=0) == 5)
elapsed = time() - start
print(f"vectorized computation took {elapsed:.3} seconds")

print(observations / ITERATIONS)
