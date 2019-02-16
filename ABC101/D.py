N, M = map(int, input().split())
X, Y, Z = [], [], []
for i in range(N):
    x, y, z = map(int, input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)
 
num = -float("inf")
for i in [-1, 1]:
    for j in [-1, 1]:
        for k in [-1, 1]:
            tmp = []
            for l in range(N):
                tmp.append(i * X[l] + j * Y[l] + k * Z[l])
 
            tmp = sorted(tmp, reverse=True)
            num = max(num, sum(tmp[:M]))
 
print(num)