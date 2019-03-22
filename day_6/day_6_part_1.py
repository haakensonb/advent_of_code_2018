"""
    Advent of Code Day 6
    Part 1
"""

# test input
# data = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]

def build_grid(data):
    columns = max(data, key=lambda x: x[0])[0] + 1
    rows = max(data, key=lambda x: x[1])[1] + 1

    grid = [['.' for i in range(columns)] for i in range(rows)]

    for i in range(len(data)):
        row = data[i][1]
        column = data[i][0]
        grid[row][column] = i
    
    return grid

def find_distances():
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
                # append a tuple of the distance and it's id to the distances list
                distances.append((distance, k))
            # sort the distances from least to greatest
            sorted_distances = sorted(distances, key=lambda x: x[0])
            # if the second distance in the sorted list is the same as the first
            # that means that locations are equally far away from two or more coordinates
            if sorted_distances[0][0] == sorted_distances[1][0]:
                # so in this case make sure it is just a dot rather than a coordinate id
                grid[i][j] = '.'
            else:
                # change the value at the grid to the coordinate id of the lowest distance
                grid[i][j] = sorted_distances[0][1]
            
            # add any id in the first or last row to excluded ids
            # if an id is in any of these rows then it is treated as infinite and not need for area calc
            if i == 0 or i == len(grid)-1:
                excluded_ids.add(sorted_distances[0][1])
            # any id in the first or last column is also not needed for area calc
            if j == 0 or j == len(grid[i])-1:
                excluded_ids.add(sorted_distances[0][1])

def find_largest_area():
    # set of possible coordinate ids
    total_ids = set([x for x in range(len(data))])
    # set of coordinate ids that are in total ids but not in excluded ids
    finite_coordinates = list(total_ids - excluded_ids)
    max_area = 0
    for coordinate in finite_coordinates:
        # number of times coordinate id appears in the grid
        coor_count = sum([x.count(coordinate) for x in grid])
        if coor_count > max_area:
            max_area = coor_count
    return max_area

if __name__ == "__main__":
    # turn the input into a list of ordered pairs
    data = [(int(line.split(',')[0]), int(line.split(',')[1].strip())) for line in open('input.txt')]

    grid = build_grid(data)
    excluded_ids = set()
    find_distances()
    print(find_largest_area())
