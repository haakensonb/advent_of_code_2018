"""
    Advent of Code Day 2
    Part 2:
    Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

    The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

    abcde
    fghij
    klmno
    pqrst
    fguij
    axcye
    wvxyz
    The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij 
    differ by exactly one character, the third (h and u). Those must be the correct boxes.

    What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing 
    character from either ID, producing fgij.)
"""

data = [line.strip() for line in open("input.txt")]

# test data
# data = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

def find_common():
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            answer = check_diff(data[i], data[j])
            if answer != '':
                return answer


def check_diff(str1, str2):
    off_count = 0
    common_letters = ''
    for x in range(len(str1)):
        if off_count > 1:
            return ''
        elif str1[x] == str2[x]:
            common_letters += str1[x]
        else:
            off_count += 1
    return common_letters

# print(check_diff('fghij', 'fguij'))
print(find_common())