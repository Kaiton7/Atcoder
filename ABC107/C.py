N, K = map(int,input().split())
x = list(map(int,input().split()))

Width = N-K+1
prev = 100000000000
print(N,K)
retval = float("inf")
for i in range(0, Width):
  left = x[i]
  right = x[i + K - 1]
  time = max(abs(left), abs(right))
  if abs(left + right) != abs(left) + abs(right):
    time += min(abs(left), abs(right)) * 2
    retval = min(retval, time)
print(retval)

"""
for i in range(0,Width+1):
  tmp = min(abs(X[i])-abs(X[i] - X[i+K]))
  if(tmp<prev):
    prev=tmp
"""
print(prev)
  
