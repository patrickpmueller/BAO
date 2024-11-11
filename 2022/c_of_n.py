#!/bin/env python

import math

n = int(input())
count = 0

for a in range(0, math.ceil(math.sqrt(n))):
    for b in range(0, math.ceil(math.sqrt(n))):
        if a**2 + b**2 < n:
            count += 1

print(count)
