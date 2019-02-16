N,K = map(int,input().split(" "))
H = list(map(int,input().split(" ")))
#DPテーブル作成
dp = [0]*(len(H))

if(len(H)<=K):
    print(abs(H[-1]-H[0]))
else:
    for i in range(K):
        # K番目までは0番目から引けばいい
        dp[i] = abs(H[i] - H[0])
    for i in range(K,len(H)):
        res=1000000
        for j in range(1,K+1):
            res = min(res,abs(dp[i-j]) + abs(H[i-j] - H[i]))
        dp[i] = res 
    # dp[i] = min(dp[i-2] + abs(H[i-2] - H[i]) ,dp[i-1] + abs(H[i-1] - H[i]))

    print(dp[len(H)-1])
#print(dp)