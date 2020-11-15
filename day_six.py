def read_input(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            left, right = line.split(')')
            if(orbits.get(left) is not None):
                orbits[left].append(right.strip())
            else:
                orbits[left] = [right.strip()]

orbits={}

count=0

def rec_count(orb):
    for p in orb:
        global count
        count+=1
        if(orbits.get(p) is not None):
            rec_count(orbits[p])


read_input('in.txt')
for k,v in orbits.items():
    rec_count(v)
print(count)