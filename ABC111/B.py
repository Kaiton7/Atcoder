import collections
n=int(input())
N=list(map(int,input().split(" ")))
list_odd=N[::2]
list_even=N[1::2]
c_odd = collections.Counter(list_odd)
c_even = collections.Counter(list_even)
most_odd=c_odd.most_common()[0][1]
most_even=c_even.most_common()[0][1]
if (n<=2):
    print("0")
elif (len(list_even)==most_even and len(list_odd)==most_odd and c_odd.most_common()[0][0]==c_even.most_common()[0][0]):
    print(most_odd)
else:
    if(c_odd.most_common()[0][0]==c_even.most_common()[0][0]):
        M=max(c_odd.most_common()[1][1],c_even.most_common()[1][1])
        print(min((len(list_even)+len(list_odd)-M-most_odd),(len(list_even)+len(list_odd)-M-most_even)))
    else:
        print(len(list_even)+len(list_odd)-most_even-most_odd)
#c_odd.most_common()[0][0]==c_even.most_common()[0][0]