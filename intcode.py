#!/usr/bin/python

import argparse
import queue
import string
import sys
import threading

def intcode(program):
    in_queue = queue.Queue()
    out_queue = queue.Queue()

    t = threading.Thread(target=base_intcode, args=(program, in_queue, out_queue))
    t.start()

    running = True
    while running:
        msg = out_queue.get()
        if msg["action"] == "exit":
            running = False
            t.join()
        elif msg["action"] == "error":
            running = False
            print(str(msg["error"]))
            t.join()
        elif msg["action"] == "request":
            msg["action"] = "response"
            msg["value"] = input("Enter an integer value: ")
            in_queue.put(msg)
        elif msg["action"] == "output":
            print(str(msg["value"]))
        else:
            print("Unknown action: " + msg["action"])

class UnknownOpcode(Exception):
    def __init__(self, opcode):
        self.opcode = opcode

class UnknownMode(Exception):
    def __init__(self, mode):
        self.mode = mode

class UnboundedList(list):
    def __init__(self, data):
        self.data = data
    def _access(self, idx):
        if idx < 0:
            raise IndexError
        if idx >= len(self):
            self.data.extend([0] * (idx - len(self.data) + 1))
    def __getitem__(self, idx):
        self._access(idx)
        return self.data[idx]
    def __setitem__(self, idx, val):
        self._access(idx)
        self.data[idx] = val
    def __len__(self):
        return len(self.data)

def base_intcode(program, in_queue, out_queue):
    index = 0
    rbase = 0

    program = UnboundedList(program)

    def get_arg(index, pos):
        mode = (program[index] // (10 ** (pos + 1))) % 10
        if mode == 0:
            return program[program[index+pos]]
        elif mode == 1:
            return program[index+pos]
        elif mode == 2:
            return program[rbase+program[index+pos]]
        else:
            raise UnknownMode(mode)

    try:
        running = True
        while running:
            op = program[index] % 100
            if op in (1, 2, 7, 8):
                arg1 = get_arg(index, 1)
                arg2 = get_arg(index, 2)
                arg3 = program[index+3]

                if op == 1:
                    program[arg3] = int(arg1) + int(arg2)
                elif op == 2:
                    program[arg3] = arg1 * arg2
                elif op == 7:
                    if arg1 < arg2:
                        program[arg3] = 1
                    else:
                        program[arg3] = 0
                elif op == 8:
                    if arg1 == arg2:
                        program[arg3] = 1
                    else:
                        program[arg3] = 0
                index += 4
            elif op == 3 or op == 4 or op == 9:
                if op == 3:
                    msg = {"action": "request"}
                    out_queue.put(msg)
                    obj = in_queue.get()
                    program[program[index+1]] = obj["value"]
                elif op == 4:
                    arg1 = get_arg(index, 1)
                    msg = {"action": "output", "value": arg1}
                    out_queue.put(msg)
                elif op == 9:
                    arg1 = get_arg(index, 1)
                    rbase += arg1
                index += 2
            elif op == 5 or op == 6:
                arg1 = get_arg(index, 1)
                arg2 = get_arg(index, 2)
                if op == 5:
                    if arg1 != 0:
                        index = arg2
                    else:
                        index += 3
                elif op == 6:
                    if arg1 == 0:
                        index = arg2
                    else:
                        index += 3
            elif op == 99:
                msg = {"action": "exit"}
                out_queue.put(msg)
                running = False
            else:
                raise UnknownOpcode(op)
    except UnknownOpcode as e:
        msg = {"action": "error", "error": "Unknown opcode: " + str(e.opcode)}
        out_queue.put(msg)
    except UnknownMode as e:
        msg = {"action": "error", "error": "Unknown mode: " + str(e.mode)}
        out_queue.put(msg)
    except IndexError:
        msg = {"action": "error", "error": "Index out of bounds"}
        out_queue.put(msg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Parse optional file inputs")
    parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
    args = parser.parse_args()

    sep = ','
    program = [int(s) for s in args.input.read().split(sep)]

    intcode(program)

    print("[" + sep.join([str(i) for i in program]) + "]")
