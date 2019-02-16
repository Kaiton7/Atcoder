import numpy as np
N, M = map(int, input().split())
p_dict = {}
p = [0 for i in range(M)]
y = [0 for i in range(M)]
i_in_p = [0 for i in range(M)]
 
for i in range(M):
    p[i], y[i] = map(int, input().split())
    if p[i] not in p_dict:
        i_in_p[i] = 0
        p_dict[p[i]] = [y[i]]
        continue
    i_in_p[i] = len(p_dict[p[i]])
    p_dict[p[i]].append(y[i])
print(p_dict)
print(i_in_p)
print("--------")
for key in p_dict.keys():
    p_dict[key] = np.array(p_dict[key]).argsort().argsort() + 1
    print(key)
    print(np.array(p_dict[key]).argsort() + 1)
print(p_dict)
print(p)

for i in range(M):
    print('{:06d}{:06d}'.format(p[i], p_dict[p[i]][i_in_p[i]]))