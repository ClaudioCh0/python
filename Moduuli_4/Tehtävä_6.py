import random

N = int(input("Anna pisteiden määrä: "))
M = 0

for i in  range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x + y < 1:
        M += 1 

pi = 4 * M / N 

print("Piinlikiarvo", pi)