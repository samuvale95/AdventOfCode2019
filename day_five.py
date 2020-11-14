operations = {
    1: (lambda a,b: a+b, 2, 4),
    2: (lambda a,b: a*b, 2, 4),
    3: (lambda: INPUT, 0, 2),
    4: (lambda a: print(a), 1, 2),
}

modes = {
    0: lambda i: program[i],
    1: lambda i: i
}

def decode(code):
    default=list('00000')
    code=list(str(code))
    for i in range(0, len(code)):
        i=(i+1)*-1
        default[i] = code[i]
    return default


def run(program):
    i=0
    while program[i] != 99 :
        par_mode = decode(program[i])

        res_mode = int(par_mode[0])
        par2_mode = int(par_mode[1])
        par1_mode = int(par_mode[2])
        opcode = int(''.join(par_mode[3:]))

        op_tuple = operations[opcode]

        if(op_tuple[1] == 2):
            program[modes[res_mode](i+3)] = op_tuple[0](program[modes[par1_mode](i+1)], program[modes[par2_mode](i+2)])
        elif(op_tuple[1] == 1):
            op_tuple[0](program[modes[par1_mode](i+1)])
        else:
            program[modes[par1_mode](i+1)] = op_tuple[0]()
        i+=op_tuple[2]

program = [int(i) for i in input().split(',')]
INPUT=1
run(program)