K, A, B = map(int, input().split())
count = 0
if(A >= B-2):
    # print(K+1)
    count = K+1
else:
    K = K - (A - 1)

    if(K%2==0):
        count += ((K//2)-1)*(B-A) + B
    else:
        count+=(K//2-1)*(B-A) + B
        count+=1
        # print("No")

print(count)