"""
    Advent of Code Day 3
    Part 1:

    Each Elf has made a claim about which area of fabric would be ideal for Santa's suit.
    All claims have an ID and consist of a single rectangle with edges parallel to the edges 
    of the fabric. Each claim's rectangle is defined as follows:

        The number of inches between the left edge of the fabric and the left edge of the rectangle.
        The number of inches between the top edge of the fabric and the top edge of the rectangle.
        The width of the rectangle in inches.
        The height of the rectangle in inches.

    A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the 
    left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it 
    claims the square inches of fabric represented by # (and ignores the square inches of fabric
    represented by .) in the diagram below:

    ...........
    ...........
    ...#####...
    ...#####...
    ...#####...
    ...#####...
    ...........
    ...........
    ...........

    The problem is that many of the claims overlap, causing two or more claims to cover part of the 
    same areas. For example, consider the following claims:

    #1 @ 1,3: 4x4
    #2 @ 3,1: 4x4
    #3 @ 5,5: 2x2

    Visually, these claim the following areas:

    ........
    ...2222.
    ...2222.
    .11XX22.
    .11XX22.
    .111133.
    .111133.
    ........

    The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent
    to the others, does not overlap either of them.)

    If the Elves all proceed with their own plans, none of them will have enough fabric. How many 
    square inches of fabric are within two or more claims?
"""


def build_coordinates():
    coordinates = {}

    for line in data:
        # parse line for starting x and y coordinates
        starting_split = line[2].split(',')
        start_x = int(starting_split[0])
        # have to split again to get y coordinate
        start_y = int(starting_split[1].split(':')[0])
        # parse line for rectangle dimensions
        dimension_split = line[3].split('x')
        width = int(dimension_split[0])
        height = int(dimension_split[1])
        # print(start_x, start_y, width, height)

        # build coordinates
        # add one to everything to get the actual coordinates that are contained inside the sheet instead of coordinates that mark border as well
        for i in range(start_x + 1, start_x + width + 1):
            for j in range(start_y + 1, start_y + height + 1):
                coordinate_pair = str((i, j))
                if coordinate_pair in coordinates:
                    coordinates[coordinate_pair] += 1
                else:
                    coordinates[coordinate_pair] = 1

    return coordinates


def get_num_overlapping(coordinates):
    num_overlapping = 0
    for coordinate_pair, value in coordinates.items():
        if value >= 2:
            num_overlapping += 1
    return num_overlapping


if __name__ == "__main__":

    # test data
    # data = [line.split() for line in open("test_input.txt")]

    data = [line.split() for line in open("input.txt")]
    coordinates = build_coordinates()
    print(get_num_overlapping(coordinates))


