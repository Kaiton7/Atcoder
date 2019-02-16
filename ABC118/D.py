N,M = list(map(int,input().split()))
A = list(map(int,input().split()))

Mach = {2,5,5,4,5,6,3,7,6}
L=[]
for i in A:
    L.append(Mach[i-1])
print(Mach[4])
print(L)