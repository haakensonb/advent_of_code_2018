"""
    Advent of Code Day 2
    Part 1:
    Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if you were 
    discovered - and use your fancy wrist device to quickly scan every box and produce a list of the likely candidates (your puzzle input).

    To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing 
    exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two 
    counts together to get a rudimentary checksum and compare it to what your device predicts.

    For example, if you see the following box IDs:

    abcdef contains no letters that appear exactly two or three times.
    bababc contains two a and three b, so it counts for both.
    abbcde contains two b, but no letter appears exactly three times.
    abcccd contains three c, but no letter appears exactly two times.
    aabcdd contains two a and two d, but it only counts once.
    abcdee contains two e.
    ababab contains three a and three b, but it only counts once.
    Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times.
    Multiplying these together produces a checksum of 4 * 3 = 12.

    What is the checksum for your list of box IDs?
"""

data = [line.strip() for line in open("input.txt")]

# test data
# data = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']

def get_check_sum():
    num_of_twos, num_of_threes = 0, 0
    for line in data:
        unique_letters = set(line)
        two_found, three_found = False, False
        for letter in unique_letters:
            # only want to increment if we haven't already found a letter that appears 3 times
            if (line.count(letter) == 3) and (three_found == False):
                three_found = True
                num_of_threes += 1
            
            # only want to increment if we haven't already found a letter that appears 2 times
            if (line.count(letter) == 2) and (two_found == False):
                two_found = True
                num_of_twos += 1
    return num_of_twos * num_of_threes

print(get_check_sum())