import re

with open('j3input.txt', 'r') as f:
    lines = f.readlines()

c = 0
enable = True

for line in lines:
    matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', line)
    for match in matches:
        if enable and match.startswith('mul'):
            prod = 1
            factors = re.findall(r'([0-9]{1,3})', match)
            for f in factors:
                prod *= int(f)
            c += prod
        elif match.startswith('don'):
            enable = False
        elif match.startswith('do'):
            enable = True

print(c)