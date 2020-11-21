#!/usr/bin/python

import argparse
import math
import sys

def fuel(mass):
    return math.floor(mass / 3) - 2

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

sum = 0
for line in args.input:
    sum += fuel(int(line))

print("Fuel: " + str(sum))
