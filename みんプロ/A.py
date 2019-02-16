N, K = map(int, input().split())
if(N%2==1):
    if(N//2 + 1 >= K):
        print("YES")
    else:
        print("NO")
else:
    if(N//2 >= K):
        print("YES")
    else:
        print("NO")

# print(N//2)