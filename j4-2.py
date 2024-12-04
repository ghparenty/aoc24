with open('j4input.txt', 'r') as f:
    lines = f.readlines()

c_grid = []
c = 0

for line in lines:
    c_grid.append(list(line.strip()))

for i in range(1, len(c_grid)-1):
    for j in range(1, len(c_grid[0])-1):
        if c_grid[i][j] == 'A':
            word1 = c_grid[i-1][j-1] + c_grid[i][j] + c_grid[i+1][j+1]
            word2 = c_grid[i-1][j+1] + c_grid[i][j] + c_grid[i+1][j-1]
            if (word1 == 'MAS' or word1 == 'SAM') and (word2 == 'MAS' or word2 == 'SAM'):
                c += 1
print(c)