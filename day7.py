#!/usr/bin/python

import argparse
import queue
import sys

from intcode import base_intcode

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

sep = ','
program = [int(s) for s in args.input.read().split(sep)]

maximum = 0
for a in range(0, 5):
    a_in = queue.Queue()
    a_out = queue.Queue()
    a_program = program.copy()

    msg = {"action": "response", "value": a}
    a_in.put(msg)
    msg = {"action": "response", "value": 0}
    a_in.put(msg)
    base_intcode(a_program, a_in, a_out)
    a_out.get()
    a_out.get()
    a_ret = a_out.get()

    for b in range(0, 5):
        if b == a:
            continue

        b_in = queue.Queue()
        b_out = queue.Queue()
        b_program = program.copy()

        msg = {"action": "response", "value": b}
        b_in.put(msg)
        msg = {"action": "response", "value": a_ret["value"]}
        b_in.put(msg)
        base_intcode(b_program, b_in, b_out)
        b_out.get()
        b_out.get()
        b_ret = b_out.get()

        for c in range(0, 5):
            if c == b or c == a:
                continue

            c_in = queue.Queue()
            c_out = queue.Queue()
            c_program = program.copy()

            msg = {"action": "response", "value": c}
            c_in.put(msg)
            msg = {"action": "response", "value": b_ret["value"]}
            c_in.put(msg)
            base_intcode(c_program, c_in, c_out)
            c_out.get()
            c_out.get()
            c_ret = c_out.get()

            for d in range(0, 5):
                if d == c or d == b or d == a: 
                    continue

                d_in = queue.Queue()
                d_out = queue.Queue()
                d_program = program.copy()

                msg = {"action": "response", "value": d}
                d_in.put(msg)
                msg = {"action": "response", "value": c_ret["value"]}
                d_in.put(msg)
                base_intcode(d_program, d_in, d_out)
                d_out.get()
                d_out.get()
                d_ret = d_out.get()

                for e in range(0, 5):
                    if e == d or e == c or e == b or e == a:
                        continue

                    e_in = queue.Queue()
                    e_out = queue.Queue()
                    e_program = program.copy()

                    msg = {"action": "response", "value": e}
                    e_in.put(msg)
                    msg = {"action": "response", "value": d_ret["value"]}
                    e_in.put(msg)
                    base_intcode(e_program, e_in, e_out)
                    e_out.get()
                    e_out.get()
                    e_ret = e_out.get()

                    if e_ret["value"] > maximum:
                        maximum = e_ret["value"]

print("Maximum: " + str(maximum))
