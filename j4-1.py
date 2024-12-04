with open('j4input.txt', 'r') as f:
    lines = f.readlines()

c_grid = []
c = 0

for line in lines:
    c_grid.append(list(line.strip()))

for i in range(len(c_grid)):
    for j in range(len(c_grid[0])):
        if j < len(c_grid[0])-3:
            word = c_grid[i][j] + c_grid[i][j+1] + c_grid[i][j+2] + c_grid[i][j+3]
            if word == 'XMAS' or word == 'SAMX':
                c += 1
        if i < len(c_grid)-3:
            word = c_grid[i][j] + c_grid[i+1][j] + c_grid[i+2][j] + c_grid[i+3][j]
            if word == 'XMAS' or word == 'SAMX':
                c += 1
        if j < len(c_grid[0])-3 and i < len(c_grid)-3:
            word = c_grid[i][j] + c_grid[i+1][j+1] + c_grid[i+2][j+2] + c_grid[i+3][j+3]
            if word == 'XMAS' or word == 'SAMX':
                c += 1
        if i < len(c_grid)-3 and j > 2:
            word = c_grid[i][j] + c_grid[i+1][j-1] + c_grid[i+2][j-2] + c_grid[i+3][j-3]
            if word == 'XMAS' or word == 'SAMX':
                c += 1
print(c)