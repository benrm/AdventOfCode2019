import math
import sys

def fuel(mass):
    return math.floor(mass / 3) - 2

sum = 0
for line in sys.stdin:
    sum += fuel(int(line))

print("Fuel: " + str(sum))
