
import re

def never_decrease(pwd):
    pwd = list(pwd)
    a=pwd[0]
    for i in range(1, len(pwd)):
        if a>pwd[i]: return False
        else: a=pwd[i]
    return True

def near_double(pwd):
    if len(re.search(r'\d*\d{2}\d*', str(pwd))) > 0: return True
    else: return False

def new_near_double(x):
    for i in range(len(x)-1):
        for i in range(len(x)-1):
            if x[i] == x[i+1]:
                if (i > 0 and x[i-1] == x[i]) or (i < len(x) - 2 and x[i+2] == x[i+1]):
                    continue
                else:
                    return True

def check_password():
    cnt=0
    for pwd in range(357253, 892942):
        if(never_decrease(str(pwd)) and new_near_double(str(pwd))): cnt+=1
    print(cnt)

check_password()