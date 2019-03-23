"""
    Advent of Code Day 7
    Part 1
"""

"""
    algorithm:
    -parse input into adjacency list
    -compute the indegree of all vertices
    -place vertices with initial indegree of 0 into box(queue)
    -while the queue is not empty, deque, print key, update adjacent indegrees
    -use alphabetical order to break ties, use insertion sort to enqueue?

    data:
    graph (list)
    vertex class:
        key containing letter
        number of indegrees
        list of adjacent vertices (list of edges)
    queue (list)
"""

vertices = {}

def enqueueInsertionSort(myQueue, myTuple):
    step = myTuple[0]
    # if the queue is empty
    if not myQueue:
        # then just add the data
        myQueue.append(myTuple)
    # otherwise have to find correct place in list
    else:
        # start the target index at 0
        index = 0
        # for every item in the queue
        for item in myQueue:
            # if the number we want to insert is bigger than the current number
            # that means it doesn't go here, but somewhere after the current number 
            if step > item[0]:
                # so move the target index up
                index += 1
            # otherwise we have moved the target index as much as needed
            else:
                # so just stop iterating through the queue
                break
        # insert the data wherever the target index ended up
        myQueue.insert(index, myTuple)       

def parse_input(file_name):
    with open(file_name) as file:
        for line in file:
            line = line.split()
            first_step = line[1]
            second_step = line[-3]
            # create adjacency list
            if first_step not in vertices:
                vertices[first_step] = [0, []]
            if second_step not in vertices:
                vertices[second_step] = [0, []]
            vertices[first_step][1].append(second_step)

def calc_indegree():
    for key, value in vertices.items():
        edges = vertices[key][1]
        for edge in edges:
            if edge in vertices:
                vertices[edge][0] += 1

parse_input("input.txt")
calc_indegree()

# place all vertices with an indegree of 0 in the queue
queue = []
# queue = [enqueueInsertionSort(queue, (key, value[0])) for key, value in vertices.items() if value[0] == 0]
for key,value in vertices.items():
    if value[0] == 0:
        enqueueInsertionSort(queue, (key, value[0]))

# print(vertices)
# enqueueInsertionSort(queue, ("A", 0))
# enqueueInsertionSort(queue, ("D", 0))
# print(queue)
output = ""
# while(queue):
#     print(queue)
#     # queue = sorted(queue)
#     dequeuedItem = queue.pop(0)
#     # print(dequeuedItem[0])
#     output += dequeuedItem[0]
#     adjacent_edges = vertices[dequeuedItem[0]][1]
#     for edge in adjacent_edges:
#         vertices[edge][0] -= 1
#         if vertices[edge][0] == 0:
#             enqueueInsertionSort(queue, (edge, 0))
#             # queue.append((edge, 0))
keep_going = True
while(keep_going):
    # print(queue)
    if not queue:
        keep_going = False
    else:
        dequeuedItem = queue.pop(0)
        output += dequeuedItem[0]
        adjacent_edges = vertices[dequeuedItem[0]][1]
        for edge in adjacent_edges:
            print(queue)
            vertices[edge][0] -= 1
            if vertices[edge][0] == 0:
                enqueueInsertionSort(queue, (edge, 0))

print(output)