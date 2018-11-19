A=list(map(int,input().split(' ')))

Max=max(A)
Min=min(A)
A.remove(Max)
A.remove(Min)

print(10*Max+Min+A[0])


