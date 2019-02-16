N, M = list(map(int,input().split()))
X = list(map(int,input().split()))

X.sort()
# 各点の間隔
Inter = [X[i+1]-X[i] for i in range(M-1)]
Inter.sort()

tmp=0
res=X[-1]-X[0]
# コマの個数が多ければ0
if(N>=M):
    print("0")
elif(N==1):
    print(res)
#コマの数2個以上
else:
    for i in range(N-1):
        tmp+=Inter[M-(i+2)]
    print(res-tmp)