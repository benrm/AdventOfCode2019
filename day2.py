import string
import sys

sep = ','
program = [int(s) for s in sys.stdin.read().split(sep)]

if len(program) < 4:
    print("Program is too short.")
    exit(1)

program[1] = 12
program[2] = 2

index = 0
while program[index] != 99:
    op, arg1, arg2, save = program[index:index+4]
    if op == 1:
        program[save] = program[arg1] + program[arg2]
    elif op == 2:
        program[save] = program[arg1] * program[arg2]
    elif op == 99:
        break
    index += 4

print("[" + sep.join([str(i) for i in program]) + "]")
