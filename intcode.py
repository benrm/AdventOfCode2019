def get_arg(index, pos):
    mode = (program[index] // (10 ** (pos + 1))) % 10
    if mode == 0:
        return program[program[index+pos]]
    elif mode == 1:
        return program[index+pos]

def intcode(program):
    index = 0
    while program[index] != 99:
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
        elif op == 3 or op ==4:
            if op == 3:
                program[program[index+1]] = input("Provide an integer: ")
            elif op == 4:
                arg1 = get_arg(index, 1)
                print(str(arg1))
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
            break
        else:
            print("Unknown opcode")
            break
