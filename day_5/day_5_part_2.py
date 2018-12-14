"""
    Advent of Code Day 5
    Part 2
"""
import string


def is_opposite_polarity(unit_1, unit_2):
    if (unit_1.islower() and unit_2.isupper()):
        if(unit_1 == unit_2.lower()):
            return True
    elif (unit_1.isupper() and unit_2.islower()):
        if(unit_1.lower() == unit_2):
            return True
    return False


def breakdown_polymers(polymer):
    stack = []

    for unit in polymer:
        # if there is an item on the top of the stack then pass that and the currentunit 
        # to the polarity checking function
        if len(stack) > 0 and is_opposite_polarity(stack[-1], unit):
            # if the units are opposite polarities 
            stack.pop()
        else:
            stack.append(unit)

    return stack

# not very efficient but works
def shortest_filtered_polymer(polymer):
    filtered_polymer_lengths = []
    alpha = string.ascii_lowercase
    for letter in alpha:
        filtered_data = [unit for unit in polymer if unit.lower() != letter]
        filtered_data = breakdown_polymers(filtered_data)
        filtered_polymer_lengths.append(len(filtered_data))
    
    return min(filtered_polymer_lengths)

if __name__ == "__main__":
    # test input
    # data = 'dabAcCaCBAcCcaDA'

    # real input
    data = list(open("input.txt").read().strip())

    print(shortest_filtered_polymer(data))


