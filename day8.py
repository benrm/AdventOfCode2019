#!/usr/bin/python

import argparse
import math
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
parser.add_argument("--width", type=int)
parser.add_argument("--height", type=int)
args = parser.parse_args()

data = args.input.read()

idx = 0
size = args.width * args.height

layers = []
while idx + size < len(data):
    layers.append(data[idx:idx+size])
    idx += size

least_layer = -1
least = size
for idx in range(len(layers)):
    if layers[idx].count("0") <= least:
        least_layer = idx
        least = layers[idx].count("0")

print(str(layers[least_layer].count("1")*layers[least_layer].count("2")))
