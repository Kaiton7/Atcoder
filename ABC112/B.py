from sys import stdin
import numpy as np

N,T = map(int,input().split(" "))

#data = [int(x) for x in stdin.readline().rstrip().split() for _ in range(N)]
data=[]
for i in range(N):
    data.append(list(map(int,input().split(" "))))
arr = np.array(data)

j=0
print(arr)
#for i in range(N):
print(np.(arr))
print(np.min(arr,axis=0))
print("daew")
print("faf")