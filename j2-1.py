with open('j2input.txt', 'r') as f:
    lines = f.readlines()

c = 0

for line in lines:
    good = True
    dir_ctr = 0
    l_str = line.split()
    l = []
    for k in l_str:
        l.append(float(k))
    for i in range(len(l)-1):
        gap = abs(l[i+1] - l[i])
        if 1 <= gap <= 3:
            if l[i] > l[i+1]:
                dir_ctr += 1
            elif l[i] < l[i+1]:
                dir_ctr -= 1
        else:
            good = False
            break
    good = good and abs(dir_ctr) == len(l)-1
    if good:
        c += 1

print(c)