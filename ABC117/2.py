N = int(input())
L = list(map(int,input().split()))
ans = True



for i in range(N):
    if(L[i] >= sum(L)-L[i]):
        ans = False

if(ans):
    print("Yes")
else:
    print("No")