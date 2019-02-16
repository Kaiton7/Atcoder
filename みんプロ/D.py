L = int(input())
A = [int(input()) for i in range(L)]
# print(A)

# 始まるところで分けて咲き進む方で奇数なら1,偶数なら0、後から進む方はその逆、最後尾に0があればそれは数えない

res=10**9
left_back=0
left_first=0
right_first=0
right_back=0
t=0
#print(A)
index=0
for i in A:
    if(index==0 and i== 0):
        flag=1
        t+=1
        #print("A:",i)
    elif(i==0 and flag==1):
        t+=1
        #print("B:",i)
    else:
        flag = 0
        #print("C;",i)
    index+=1

A = A[t:]
A = A[::-1]
# print(A)
t=0
index=0
for i in A:
    if(index==0 and i== 0):
        flag=1
        t+=1
        #print("A:",i)
    elif(i==0 and flag==1):
        t+=1
        #print("B:",i)
    else:
        flag = 0
        #print("C;",i)
    index+=1

A = A[t:]
A = A[::-1]
# rint(A)
# 逆順OK
left_right=0
right_left=0
res_p=0
i_res=0
for i in range(L):
    left_right=0
    right_left=0
    left_back=0
    left_first=0
    right_first=0
    right_back=0    
    for j in A[:i]:
        #print(j)
        left_first += j%2
        if(j%2==0):
            left_back += 1
        if(j==0):
            left_first +=1
    if(A[0]%2==0):
        left_back-=1
    #print(":::")

    for k in A[i:]:
        #print(k)
        right_first += k%2
        
        if(k%2==0):
            right_back += 1
        if(k==0):
            right_first+=1
    if(A[-1]%2==0):
        right_back-=1
    # print(A[0],A[-1])
    
    left_right = left_first+right_back
    right_left = right_first + left_back
    res_p=res
    res = min(res,left_right,right_left)
    if(res<res_p):
        i_res=i

    #print("====")
print(res)
# print(i_res)
# print(0//2)
#print(A[i_res::])
#for i in A[i_res::]:
    #print(i%2)