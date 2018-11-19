
from functools import reduce
from fractions import gcd

N,X = map(int,input().split(" "))
x = list(map(int,input().split(" ")))
Y = [abs(i-X) for i in x]

print(reduce(gcd, Y, 0))