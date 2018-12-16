"""
    Advent of Code Day 6
    Part 2
"""


def build_grid(data):
    columns = max(data, key=lambda x: x[0])[0] + 1
    rows = max(data, key=lambda x: x[1])[1] + 1

    grid = [['.' for i in range(columns)] for i in range(rows)]

    for i in range(len(data)):
        row = data[i][1]
        column = data[i][0]
        grid[row][column] = i
    
    return grid

def get_region_size(max_total_distance):
    region_size = 0
    # loop through grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            distances = []
            # for every coordinate id in the data
            for k in range(len(data)):
                grid_x = j
                grid_y = i
                data_x = data[k][0]
                data_y = data[k][1]
                # find manhattan distance between this coordinate and one of the data points
                distance = abs(grid_x - data_x) + abs(grid_y - data_y)
                distances.append(distance)
            total_distance = sum(distances)
            if total_distance < max_total_distance:
                region_size += 1
    return region_size


if __name__ == "__main__":
    # test input
    # data = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]
    # turn the input into a list of ordered pairs
    data = [(int(line.split(',')[0]), int(line.split(',')[1].strip())) for line in open('input.txt')]

    grid = build_grid(data)
    print(get_region_size(10000))
