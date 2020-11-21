#!/usr/bin/python

import argparse
import math
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
parser.add_argument("-r", "--recursive", action="store_true")
args = parser.parse_args()

def fuel(mass):
    ret = math.floor(mass / 3) - 2
    if args.recursive:
        if ret <= 0:
            return 0
        else:
            return ret + fuel(ret)
    else:
        return ret

sum = 0
for line in args.input:
    sum += fuel(int(line))

print("Fuel: " + str(sum))
