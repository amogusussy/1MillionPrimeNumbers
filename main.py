#!/usr/bin/python3

p = [3, 5, 7, 11, 13, 17, 19, 23, 29]

def isDivisable(a: int, listObj: list):
    for item in listObj:
        if a % item == 0: 
            return True
    return False

num = p[-1]
count = 0

while count < 1000000:
    if not isDivisable(num, p):
        p.append(num)
        print(num)
        count += 1
    num += 2


print(p)
with open('primes.txt', 'w') as f:
    f.write(str(p) + "\n")
