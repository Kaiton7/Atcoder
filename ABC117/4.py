N, K = list(map(int,input().split()))
A = list(map(int,input().split()))
tmp = 1
count = 0
# Ki以下の2の累乗数を求める
for i in range(K):
    tmp = tmp*2
    count += 1
    if(K<tmp):
        break   
count = count-1
K_max=2**count
print(count)
# print(count)

# Kが与えられる、K以下の整数にkついてA XOR k の最大値を考える
# 最上位ビットが1なら意味がないので
# 16を表すときに5bit必要だよね
ans = 0
for i in A:
    # print("len",len(b)-2)
    #print(i,b)
    if(K>i):
        # ans += int(2**count ^ i, 2)
        print(K_max ^ i)
        ans += (K_max ^ i)
    elif(K==i):
        print(0^i)
        ans += (0 ^ i)
    else:
        count = count+1
        print(i)
        sr = bin(i)
        a = sr.replace("0","2")
        a = a.replace("1","0")
        # a = "0b"+a.replace("2","1")[2:]
        a = a.replace("2","1")[-count:]
        print(a)
        i_i = int(a,2) 
        i =2
        while(K >= i-i):
            if(bin(i_i)[-i]=="1"):
                i_i= int(bin(i_i)[-i:]+"0"+bin(i_i)[-i+1:],2)
            else:
                i_i= int(bin(i_i)[-i:]+"1"+bin(i_i)[-i+1:],2)
            i+=1
        print(i_i)
        ans += (i_i ^ i)
        print(bin(i))
        print(ans)
        print("====")
print(ans)
        