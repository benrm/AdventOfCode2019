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

def dummy_func(program):
    for noun in range(0, 99):
        for verb in range(0, 99):
            newprogram = program.copy()
            newprogram[1] = noun
            newprogram[2] = verb
            intcode(newprogram)
            if newprogram[0] == 19690720:
                return noun, verb
    return 0, 0

noun, verb = dummy_func(program)
print(100 * noun + verb)
