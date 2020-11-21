#!/usr/bin/python

import argparse
import queue
import sys
import threading

from intcode import base_intcode

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

sep = ','
program = [int(s) for s in args.input.read().split(sep)]

maximum = 0
for a in range(5, 10):

    for b in range(5, 10):
        if b == a:
            continue

        for c in range(5, 10):
            if c == b or c == a:
                continue

            for d in range(5, 10):
                if d == c or d == b or d == a: 
                    continue

                for e in range(5, 10):
                    if e == d or e == c or e == b or e == a:
                        continue

                    a_in = queue.Queue()
                    a_out = queue.Queue()
                    a_program = program.copy()

                    a_thread = threading.Thread(target=base_intcode, args=(a_program, a_in, a_out))
                    a_thread.start()

                    b_in = queue.Queue()
                    b_out = queue.Queue()
                    b_program = program.copy()

                    b_thread = threading.Thread(target=base_intcode, args=(b_program, b_in, b_out))
                    b_thread.start()

                    c_in = queue.Queue()
                    c_out = queue.Queue()
                    c_program = program.copy()

                    c_thread = threading.Thread(target=base_intcode, args=(c_program, c_in, c_out))
                    c_thread.start()

                    d_in = queue.Queue()
                    d_out = queue.Queue()
                    d_program = program.copy()

                    d_thread = threading.Thread(target=base_intcode, args=(d_program, d_in, d_out))
                    d_thread.start()

                    e_in = queue.Queue()
                    e_out = queue.Queue()
                    e_program = program.copy()

                    e_thread = threading.Thread(target=base_intcode, args=(e_program, e_in, e_out))
                    e_thread.start()

                    a_out.get()
                    msg = {"action": "response", "value": a}
                    a_in.put(msg)

                    b_out.get()
                    msg = {"action": "response", "value": b}
                    b_in.put(msg)

                    c_out.get()
                    msg = {"action": "response", "value": c}
                    c_in.put(msg)

                    d_out.get()
                    msg = {"action": "response", "value": d}
                    d_in.put(msg)

                    e_out.get()
                    msg = {"action": "response", "value": e}
                    e_in.put(msg)

                    a_out.get()
                    msg = {"action": "response", "value": 0}
                    a_in.put(msg)
                    a_ret = a_out.get()

                    value = 0
                    while True:
                        msg = b_out.get()
                        if msg["action"] == "request":
                            msg = {"action": "response", "value": a_ret["value"]}
                            b_in.put(msg)
                            b_ret = b_out.get()
                            value = b_ret["value"]
                        else:
                            break

                        msg = c_out.get()
                        if msg["action"] == "request":
                            msg = {"action": "response", "value": b_ret["value"]}
                            c_in.put(msg)
                            c_ret = c_out.get()
                            value = c_ret["value"]
                        else:
                            break

                        msg = d_out.get()
                        if msg["action"] == "request":
                            msg = {"action": "response", "value": c_ret["value"]}
                            d_in.put(msg)
                            d_ret = d_out.get()
                            value = d_ret["value"]
                        else:
                            break

                        msg = e_out.get()
                        if msg["action"] == "request":
                            msg = {"action": "response", "value": d_ret["value"]}
                            e_in.put(msg)
                            e_ret = e_out.get()
                            value = e_ret["value"]
                        else:
                            break

                        msg = a_out.get()
                        if msg["action"] == "request":
                            msg = {"action": "response", "value": e_ret["value"]}
                            a_in.put(msg)
                            a_ret = a_out.get()
                            value = a_ret["value"]
                        else:
                            break

                    if value > maximum:
                        maximum = value

print("Maximum: " + str(maximum))
