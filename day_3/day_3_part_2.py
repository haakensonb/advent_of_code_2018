"""
    Advent of Code Day 3
    Part 2:

    Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch 
    of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will 
    be able to make Santa's suit after all!

    For example, in the claims above, only claim 3 is intact after all claims are made.

    What is the ID of the only claim that doesn't overlap?
"""

overlapping_ids = set()

def build_coordinates():
    coordinates = {}

    for line in data:
        claim_id = line[0].split('#')[1]
        # parse line for starting x and y coordinates
        starting_split = line[2].split(',')
        start_x = int(starting_split[0])
        # have to split again to get y coordinate
        start_y = int(starting_split[1].split(':')[0])
        # parse line for rectangle dimensions
        dimension_split = line[3].split('x')
        width = int(dimension_split[0])
        height = int(dimension_split[1])
        # print(claim_id, start_x, start_y, width, height)

        # build coordinates
        # add one to everything to get the actual coordinates that are contained inside the sheet instead of coordinates that mark border as well
        for i in range(start_x + 1, start_x + width + 1):
            for j in range(start_y + 1, start_y + height + 1):
                coordinate_pair = str((i, j))
                if coordinate_pair in coordinates:
                    coordinates[coordinate_pair]["num"] += 1
                    overlapping_ids.add(coordinates[coordinate_pair]["claim_id"])
                    overlapping_ids.add(claim_id)
                else:
                    coordinates[coordinate_pair] = {"num": 1, "claim_id": claim_id}

    return coordinates


def get_num_overlapping(coordinates):
    num_overlapping = 0
    for coordinate_pair, value in coordinates.items():
        if value["num"] >= 2:
            num_overlapping += 1
    return num_overlapping


def get_non_overlapping(coordinates):
    non_overlapping_id = ''
    for coordinate_pair, value in coordinates.items():
        if value["claim_id"] not in overlapping_ids:
            non_overlapping_id = value["claim_id"]        
    return non_overlapping_id


if __name__ == "__main__":

    # test data
    # data = [line.split() for line in open("test_input.txt")]

    data = [line.split() for line in open("input.txt")]
    coordinates = build_coordinates()
    print("Number of inches overlapping: {}".format(get_num_overlapping(coordinates)))

    print("Id of claim with no overlap: {}".format(get_non_overlapping(coordinates)))
