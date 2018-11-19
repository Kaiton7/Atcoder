N = int(input())
T,A = map(int,input().split())
X = list(map(int,input().split()))
res = 100000000
j = 1
for i in X:
    a = abs(A - (T-i*0.006))
    if(res > a):
        res = a
        res1=j        
    j+=1
print(res1)


