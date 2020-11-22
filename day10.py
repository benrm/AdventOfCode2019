#!/usr/bin/python

import argparse
import math
import string
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

x = 0
y = 0

asteroids = []

for line in args.input.readlines():
    x = 0
    for char in line:
        if char == "#":
            asteroids.append((x,y))
        x += 1
    y += 1

maximum = 0
for base in asteroids:
    angles = set()
    for target in asteroids:
        if base == target:
            continue
        x = target[0] - base[0]
        y = target[1] - base[1]
        if x == 0:
            if y > 0:
                angles.add(math.pi/2)
            else:
                angles.add(-math.pi/2)
        else:
            angle = math.atan((target[1] - base[1])/(target[0] - base[0]))
            if x < 0 and y >= 0:
                angle += math.pi
            elif x < 0 and y < 0:
                angle -= math.pi
            angles.add(angle)
    if maximum < len(angles):
        maximum = len(angles)

print("Maximum: " + str(maximum))
