# N = int(input())
A,B = list(map(int,input().split()))
#for i in range(N):
#  x,y = list(map(int,input().split()))
#  l.append([x,y])

if(B%A==0):
    print(A+B)
else:
    print(B-A)