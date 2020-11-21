#!/usr/bin/python

import argparse
import string
import sys

from intcode import intcode

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

sep = ','
program = [int(s) for s in args.input.read().split(sep)]

if len(program) < 4:
    print("Program is too short.")
    exit(1)

intcode(program)

print("[" + sep.join([str(i) for i in program]) + "]")
