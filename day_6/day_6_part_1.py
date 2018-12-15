"""
    Advent of Code Day 6
    Part 1
"""
# turn the input into a list of ordered pairs
# data = [(int(line.split(',')[0]), int(line.split(',')[1].strip())) for line in open('input.txt')]
# print(len(data))

# test input
data = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]
letters = ['A', 'B', 'C', 'D', 'E', 'F']

grid = [['.' for i in range(10)] for i in range(10)]

for i in range(len(data)):
    x = data[i][0]
    y = data[i][1]
    grid[y][x] = letters[i]

excluded_letters = set()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        distances = []
        for k in range(len(data)):
            grid_x = j
            grid_y = i
            data_x = data[k][0]
            data_y = data[k][1]
            distance = abs(grid_x - data_x) + abs(grid_y - data_y)
            distances.append((distance, letters[k]))
        sorted_distances = sorted(distances, key=lambda x: x[0])
        # print(sorted_distances)
        if sorted_distances[0][0] == sorted_distances[1][0]:
            grid[i][j] = '.'
        else:
            grid[i][j] = sorted_distances[0][1]
        
        if i == 0 or i == len(grid)-1:
            excluded_letters.add(sorted_distances[0][1])
        if j == 0 or j == len(grid[i])-1:
            excluded_letters.add(sorted_distances[0][1])

letters_set = set(letters)
finite_coordinates = list(letters_set - excluded_letters)
max_area = 0
for coordinate in finite_coordinates:
    coor_count = sum([x.count(coordinate) for x in grid])
    if coor_count > max_area:
        max_area = coor_count
print(max_area)

# for line in grid:
    # print(''.join(line))