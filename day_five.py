operations = {
    1: (lambda a,b: a+b, 2, 4, True),
    2: (lambda a,b: a*b, 2, 4, True),
    3: (lambda: INPUT, 0, 2, True),
    4: (lambda a: print(a), 1, 2, False),
    5: (lambda a,b: b if a!=0 else pc+3, 2, None, False),
    6: (lambda a,b: b if a==0 else pc+3, 2, None, False),
    7: (lambda a,b: 1 if a<b else 0, 2, 4, True),
    8: (lambda a,b: 1 if a==b else 0, 2, 4, True),
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
    global pc
    pc=0
    while program[pc] != 99 :
        par_mode = decode(program[pc])

        res_mode = int(par_mode[0])
        par2_mode = int(par_mode[1])
        par1_mode = int(par_mode[2])
        opcode = int(''.join(par_mode[3:]))

        op_tuple = operations[opcode]

        if(op_tuple[1] == 2):
            if(op_tuple[3]):
                program[modes[res_mode](pc+3)] = op_tuple[0](program[modes[par1_mode](pc+1)], program[modes[par2_mode](pc+2)])
            else:
                pc = op_tuple[0](program[modes[par1_mode](pc+1)], program[modes[par2_mode](pc+2)])
                continue
        elif(op_tuple[1] == 1):
            op_tuple[0](program[modes[par1_mode](pc+1)])
        else:
            program[modes[par1_mode](pc+1)] = op_tuple[0]()
        pc+=op_tuple[2]

program = [int(i) for i in input().split(',')]
INPUT=5
pc=0
run(program)