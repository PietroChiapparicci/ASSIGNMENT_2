import math as m
from itertools import permutations as p
def perm(n):
    set=[]
    for i in range(1,n+1):
        set.append(i)
    n_perm=m.factorial(n)
    possible_perm=p(set)
    with open("perm.txt", "w") as f:
        f.write(str(n_perm)+'\n')
        for i in possible_perm:
            f.write(' '.join(map(str,i))+'\n')
    
n=7
perm(n)