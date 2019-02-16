import numpy as np
N,M = map(int,input().split())
data=[]
for i in range(M):
    data.append(list(map(int,input().split(" "))))

arr = np.array(data)
c1=np.arange(0,M)
arr=np.insert(arr,2,c1,axis=1)
#arr_sort=arr[np.argsort(arr[:,0])]
arr_sort=arr[np.argsort(arr[:,1])]
arr_sort=arr_sort[np.argsort(arr_sort[:,0])]

j=1
i_prev=1
res=[]
k = 0
for i in arr_sort:
    if(int(i[0])!=i_prev):
        j=1
    #print("{:06}{:06}".format(i[0],j))
    test = "{:06}{:06}".format(i[0],j)
    arr_sort[k][1]= str(test)
    k+=1
    j+=1
    i_prev=i[0]

arr_sort=arr_sort[np.argsort(arr_sort[:,0])]
for i in arr_sort:
    print("{:012}".format(i[1]))