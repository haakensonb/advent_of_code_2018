# Advent of Code Day 4
# Part 2
from datetime import datetime


def get_array_of_mins():
    array_of_mins = []
    guard_index = -1
    for line in sorted_data:
        minutes = int(line.split(':')[1].split(']')[0])
        date = line[6:11]
        # guard starts shift
        if '#' in line:
            current_guard_id = line.split('#')[1].split(' ')[0]
            guard_index += 1
            guard_ids.add(current_guard_id)
            array_of_mins.append({'date': date, 'id': current_guard_id, 'mins': ['.' for _ in range(60)]})
        elif 'falls' in line:
            sleep_start = minutes
            # make sure that the date actually starts when guard falls aleep
            array_of_mins[guard_index]['date'] = date
        elif 'wakes' in line:
            sleep_end = minutes
            for value in array_of_mins:
                if (value['id'] == current_guard_id) and (value['date'] == date):
                    for i in range(sleep_start, sleep_end):
                        value['mins'][i] = '#'
    return array_of_mins


def get_guard_most_asleep(array_of_mins):
    max_sleep = 0
    max_guard = ''
    for guard in guard_ids:
        guard_sleep = 0
        for line in array_of_mins:
            if line['id'] == guard:
                guard_sleep += len(['#' for x in range(len(line['mins'])) if line['mins'][x] == '#'])
                if guard_sleep > max_sleep:
                    max_sleep = guard_sleep
                    max_guard = guard
    return max_guard


def get_min_most_asleep(array_of_mins, guard_id):
    num_of_times_asleep_at_min = [0 for _ in range(60)]
    for line in array_of_mins:
        if line['id'] == guard_id:
            for i in range(len(line['mins'])):
                if line['mins'][i] == '#':
                    num_of_times_asleep_at_min[i] += 1
    return num_of_times_asleep_at_min.index(max(num_of_times_asleep_at_min))


def get_guard_most_asleep_times_minutes(array_of_mins):
    max_guard_id = ''
    max_times_asleep = 0
    max_times_asleep_index = 0
    for guard in guard_ids:
        num_of_times_asleep_at_min = [0 for _ in range(60)]
        for line in array_of_mins:
            if line['id'] == guard:
                for i in range(len(line['mins'])):
                    if line['mins'][i] == '#':
                        num_of_times_asleep_at_min[i] += 1
        current_max = max(num_of_times_asleep_at_min)
        if current_max > max_times_asleep:
            max_times_asleep = current_max
            max_times_asleep_index = num_of_times_asleep_at_min.index(current_max)
            max_guard_id = guard
    return int(max_guard_id) * int(max_times_asleep_index)


if __name__ == "__main__":
    #test data
    # data = [line.strip() for line in open("test_input.txt")]
    # real data
    data = [line.strip() for line in open("input.txt")]

    # sort the input data by date and time
    sorted_data = sorted(
        data,
        # sort by the date in each line
        key=lambda x: datetime.strptime(x.split(']')[0].split('[')[1], '%Y-%m-%d %H:%M')
    )

    guard_ids = set()

    array_of_mins = get_array_of_mins()
    # guard_most_asleep = get_guard_most_asleep(array_of_mins)
    # min_most_asleep = get_min_most_asleep(array_of_mins, guard_most_asleep)

    # answer = int(guard_most_asleep) * int(min_most_asleep)
    # print(answer)
    print(get_guard_most_asleep_times_minutes(array_of_mins))


