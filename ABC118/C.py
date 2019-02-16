N=int(input())
A = list(map(int,input().split()))
A.sort()

# print(A)
mi = A[0]
tmp = []
for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        # print(A[i],A[j])
        tmp.append(A[j]%A[i])
tmp = [i for i in tmp if i > 0]
if(len(tmp)==0):
    print(mi)
else:
    for i in tmp:
        for j in A:
            if((j%i) < mi and j%i>0):
                mi = j%i
    print(mi)