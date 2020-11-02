
wire_a = input().split(',')
# print(wire_a)
wire_b = input().split(',')
# print(wire_b)

def right(pos, cnt): return [(pos[0]+i, pos[1], pos[2]+i) for i in range(1, cnt+1)]
def left(pos, cnt): return [(pos[0]-i, pos[1], pos[2]+i) for i in range(1, cnt+1)]
def up(pos, cnt): return [(pos[0], pos[1]+i, pos[2]+i) for i in range(1, cnt+1)]
def down(pos, cnt): return [(pos[0], pos[1]-i, pos[2]+i) for i in range(1, cnt+1)]

op={
    'R':right,
    'L':left,
    'U':up,
    'D':down
}

def process_input(wire, start):
    res=[]
    for i in range(0, len(wire)):
        pos = op[wire[i][0]](start, int(wire[i][1:]))
        res += pos
        start[0] = pos[-1][0]
        start[1] = pos[-1][1]
        start[2] = pos[-1][2]
    return res

a_positions = process_input(wire_a, [0, 0, 0])
b_positions = process_input(wire_b, [0, 0, 0])

dist_a=dict()
for i in a_positions:
    if dist_a.get((i[0], i[1])) is None: dist_a[(i[0], i[1])] = i[2]
    else:
        if dist_a.get((i[0], i[1])) > i[2]: dist_a[(i[0], i[1])] = i[2]

dist_b=dict()
for i in b_positions:
    if dist_b.get((i[0], i[1])) is None: dist_b[(i[0], i[1])] = i[2]
    else:
        if dist_b.get((i[0], i[1])) > i[2]: dist_b[(i[0], i[1])] = i[2]


inter=set([(i[0], i[1]) for i in b_positions]).intersection(set([(i[0], i[1]) for i in a_positions]))

print(min([dist_a[i] + dist_b[i] for i in list(inter)]))