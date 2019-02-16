def Res(x):
    return x / sum(map(int, str(x)))
K = int(input())
D = 0
l = 0
for i in range(K):
    D += 10**l
    print(D)
    if 10**l < Res(D+10**l):
        l += 1