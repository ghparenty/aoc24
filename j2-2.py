def float_list(l):
    l_float = []
    for k in l.split():
        l_float.append(float(k))
    return l_float

def check_report(report):
    dir_ctr = 0
    good = True
    for i in range(len(report)-1):
        gap = abs(report[i]-report[i+1])
        if 1 <= gap <= 3:
            if report[i] > report[i+1]:
                dir_ctr += 1
            elif report[i] < report[i+1]:
                dir_ctr -= 1
        else:
            good = False
            break
    return good and abs(dir_ctr) == len(report)-1

def dampener(l):
    for i in range(len(l)):
        new_l = l.copy()
        k = new_l.pop(i)
        if check_report(new_l):
            return True
    return False

with open('j2input.txt') as f:
    lines = f.readlines()

c = 0

for line in lines:
    l = float_list(line)
    if check_report(l) or dampener(l):
        c += 1

print(c)