import math

def recFuelCalc(value):
    if(value>0):
        return value+recFuelCalc(math.floor((value/3))-2)
    return 0

mass=input()
sum=0
while(mass != 'STOP'):
    sum += recFuelCalc(int(mass)) - int(mass)
    mass=input()
print(sum)