import collections
N,M = list(map(int,input().split()))
L=[]
def flatten(nested_list):
    """2重のリストをフラットにする関数"""
    return [e for inner_list in nested_list for e in inner_list]


for i in range(N):
  K = list(map(int,input().split()))
  K=K[1:]
  L.append(K)
# print(flatten(L))
cnter=collections.Counter(flatten(L))
print(len([i[0] for i in cnter.items() if i[1] >= N]))
