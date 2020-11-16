def read_input(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            left, right = line.split(')')
            if(orbits.get(left) is not None):
                orbits[left.strip()].append(right.strip())
            else:
                orbits[left.strip()] = [right.strip()]

orbits={}

def count():
    cnt=0
    def rec_count(orb):
        for p in orb:
            cnt+=1
            if(orbits.get(p) is not None):
                rec_count(orbits[p])
    for _,v in orbits.items():
        rec_count(v)
    return cnt

def search(node):
    for k,v in orbits.items():
        if(node in v):
            return k

def find_path_to_root(node, path=[]):
    path.append(node)
    for k,v in orbits.items():
        if(node in v):
            find_path_to_root(k, path)
    return path



read_input('in.txt')
you_path = find_path_to_root(search('YOU'),[])
san_path = find_path_to_root(search('SAN'),[])



is_find_path=False
while not is_find_path:
    if(you_path[-2]==san_path[-2]):
        you_path.pop()
        san_path.pop()
    else:
        print(len(set(you_path+san_path))-1)
        is_find_path=True

