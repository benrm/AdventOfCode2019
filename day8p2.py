#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
parser.add_argument("--width", type=int)
parser.add_argument("--height", type=int)
args = parser.parse_args()

data = args.input.read()

idx = 0
size = args.width * args.height
layers = int(len(data) / size)

for y in range(args.height):
    for x in range(args.width):
        for l in range(layers):
            val = data[l * size + y * args.width + x]
            if val != "2":
                if val == "0":
                    print(" ", sep="", end="")
                else:
                    print("X", sep="", end="")
                break
    print()
