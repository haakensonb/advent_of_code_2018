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
