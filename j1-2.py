from collections import Counter

with open('j1input.txt', 'r') as f:
    l = f.readlines()

l1, l2 = [], []
for i in range(len(l)):
    temp = l[i].split()
    print(temp)
    l1.append(float(temp[0]))
    l2.append(float(temp[1].replace('\n', '')))

ctr = Counter(l2)
score = 0

for i in range(len(l1)):
    if l1[i] in ctr:
        score += l1[i] * ctr[l1[i]]
print(score)
