from collections import Counter
 
S = input()
T = input()
 
s = Counter(S)
t = Counter(T)
print(s)
print(t) 
print("s.values=",s.values())
print(sorted(t.values()))
if sorted(s.values()) == sorted(t.values()):
	print("Yes")
else:
	print("No")
    