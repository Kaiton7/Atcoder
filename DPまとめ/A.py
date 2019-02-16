N = int(input())
H = list(map(int,input().split(" ")))

#DPテーブル作成
dp = [0]*(len(H))

dp[0] = 0
dp[1] = abs(H[1] - H[0])
for i in range(2,len(H)):
    dp[i] = min(dp[i-2] + abs(H[i-2] - H[i]) ,dp[i-1] + abs(H[i-1] - H[i]))

print(dp[len(H)-1])
# print(dp)