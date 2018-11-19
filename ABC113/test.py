import numpy as np
a = np.array([30,20,40,10])
print(a.argsort())
print(a[a.argsort()])
b=a[a.argsort()]
print(a.argsort().argsort())
print(b[a.argsort().argsort()])