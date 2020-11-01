
program = input().split(',')

def addition(a, b):
    return a+b

def multiply(a, b):
    return a*b

op = {
    1: addition,
    2: multiply
}

def run(first, second, prog):
    prog[1] = first
    prog[2] = second

    for i in range(0, len(prog), 4):
        if(int(prog[i])==99): break

        a = int(prog[i+1])
        b = int(prog[i+2])
        res = int(prog[i+3])
        prog[res]=op[int(prog[i])](int(prog[a]), int(prog[b]))

    return prog[0]

def searchNuonVerb(program):
    for i in range(0, 100):
        for j in range(0, 100):
            res = run(str(i), str(j), [k for k in program])
            if(int(res) == 19690720):
                return (i, j)

print(searchNuonVerb(program))