import re

with open('j3input.txt', 'r') as f:
    lines = f.readlines()

c = 0

for line in lines:
    matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line)
    for match in matches:
        prod = 1
        factors = re.findall(r'([0-9]{1,3})', match)
        for f in factors:
            prod *= int(f)
        c += prod

print(c)