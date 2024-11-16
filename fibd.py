def fibd(n,m):
    if n==1:
        return 1
    elif n==2:
        return 1
    rabbits=[0]*m
    rabbits[0]=1
    for month in range(2,n+1):
        new_gen=sum(rabbits[1:])
        rabbits[1:]=rabbits[:-1]
        rabbits[0]=new_gen
    return sum(rabbits)

n=80
m=20
result=fibd(n,m)
print(result)