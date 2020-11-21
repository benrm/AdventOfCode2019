def intcode(program):
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
