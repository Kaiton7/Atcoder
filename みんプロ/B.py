ab = [list(map(int, input().split())) for _ in range(3)]

li = []
for i in ab:
    for j in i:
        li.append(j)
res =0
for i in range(1,4):
    if(li.count(i)==2):
        res+=1

if(res==2):
    print("YES")
else:
    print("NO")
