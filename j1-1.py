import numpy as np

l = np.loadtxt('input.txt')

l1, l2 = np.sort(l[:, 0]), np.sort(l[:, 1])

l_d = []

for i in range(len(l1)):
    l_d.append(abs(l1[i] - l2[i]))

print(sum(l_d))