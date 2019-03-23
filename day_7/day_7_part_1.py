"""
    Advent of Code Day 7
    Part 1

    --- Day 7: The Sum of Its Parts ---
    You find yourself standing on a snow-covered coastline; apparently, you landed a little off course. The region is too hilly to see the North Pole from here, but you do spot some Elves that seem to be trying to unpack something that washed ashore. It's quite cold out, so you decide to risk creating a paradox by asking them for directions.

    "Oh, are you the search party?" Somehow, you can understand whatever Elves from the year 1018 speak; you assume it's Ancient Nordic Elvish. Could the device on your wrist also be a translator? "Those clothes don't look very warm; take this." They hand you a heavy coat.

    "We do need to find our way back to the North Pole, but we have higher priorities at the moment. You see, believe it or not, this box contains something that will solve all of Santa's transportation problems - at least, that's what it looks like from the pictures in the instructions." It doesn't seem like they can read whatever language it's in, but you can: "Sleigh kit. Some assembly required."

    "'Sleigh'? What a wonderful name! You must help us assemble this 'sleigh' at once!" They start excitedly pulling more parts out of the box.

    The instructions specify a series of steps and requirements about which steps must be finished before others can begin (your puzzle input). Each step is designated by a single letter. For example, suppose you have the following instructions:

    Step C must be finished before step A can begin.
    Step C must be finished before step F can begin.
    Step A must be finished before step B can begin.
    Step A must be finished before step D can begin.
    Step B must be finished before step E can begin.
    Step D must be finished before step E can begin.
    Step F must be finished before step E can begin.
    Visually, these requirements look like this:


    -->A--->B--
    /    \      \
    C      -->D----->E
    \           /
    ---->F-----
    Your first goal is to determine the order in which the steps should be completed. If more than one step is ready, choose the step which is first alphabetically. In this example, the steps would be completed as follows:

    Only C is available, and so it is done first.
    Next, both A and F are available. A is first alphabetically, so it is done next.
    Then, even though F was available earlier, steps B and D are now also available, and B is the first alphabetically of the three.
    After that, only D and F are available. E is not available because only some of its prerequisites are complete. Therefore, D is completed next.
    F is the only choice, so it is done next.
    Finally, E is completed.
    So, in this example, the correct order is CABDFE.

    In what order should the steps in your instructions be completed?
"""

class Solution1:
    def __init__(self, file_name):
        self.vertices = {}
        self.queue = []
        self.result = ""
        self.file_name = file_name

        self.parse_input()
        self.calc_indegree()
        self.init_queue()


    def insertAlphabetically(self, data):
        """
        Data is in the form of a two item list.
        The first item of the list is the step letter and the second item is the indegree of the vertex.
        Add data to the queue so that it is in alphabetical order by the array's first element
        """
        step = data[0]
        # if the queue is empty
        if not self.queue:
            # then just add the data
            self.queue.append(data)
        # otherwise have to find correct place in list
        else:
            # start the target index at 0
            index = 0
            # for every item in the queue
            for item in self.queue:
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
            self.queue.insert(index, data)       


    def parse_input(self):
        """
        Open the file and turn the step requirements into an adjacency list where each vertex is an array where
        the first item is the indegree and the second item is the list of adjacent edges
        """
        with open(self.file_name) as file:
            for line in file:
                line = line.split()
                first_step = line[1]
                second_step = line[-3]
                # create adjacency list
                # if the first_step/second_step is not in the vertices dict create vertex with 0 indegree and empty list of adjacent edges
                if first_step not in self.vertices:
                    self.vertices[first_step] = [0, []]
                if second_step not in self.vertices:
                    self.vertices[second_step] = [0, []]
                # add edge to list of adjacent edges
                self.vertices[first_step][1].append(second_step)

    def calc_indegree(self):
        """
        Go through the adjacency list and calculate the number of incoming edges for each degree (indegree)
        """
        # for every item in the adjacency list
        for key, value in self.vertices.items():
            # grab it's list of adjacent edges
            edges = self.vertices[key][1]
            # we know that all of these adjacent vertices have an indegree from the current node
            # so loop through every edge in the adjacent list
            for edge in edges:
                if edge in self.vertices:
                    # and increment the indegree
                    self.vertices[edge][0] += 1


    def init_queue(self):
        """
        Place all the vertices with an initial indegree of 0 in a list (which will be treated like a queue) alphabetically
        """
        # place all vertices with an indegree of 0 in the queue alphabetically
        queue = [self.insertAlphabetically((key, value[0])) for key, value in self.vertices.items() if value[0] == 0]
        # list comprehension written out in long form
        # for key,value in self.vertices.items():
        #     if value[0] == 0:
        #         self.insertAlphabetically((key, value[0]))


    def solve(self):
        """
        Actually compute and return the output string. Start with a queue of all vertices with an indegree of 0
        where the queue is always ordered alphabetically. Dequeue by taking the first item from the queue and add it to result string.
        Update the indegree of the adjacent vertices respectively. If the indegree of any vertice falls to 0 add it to the queue. 
        Repeat as long as there is something in the queue.
        """
        keep_going = True
        while(keep_going):
            # if there isn't anything in the queue then stop the loop
            if not self.queue:
                keep_going = False
            else:
                # dequeue the item from the front of the list
                dequeuedItem = self.queue.pop(0)
                # add it to the result string
                self.result += dequeuedItem[0]
                # grab all the adjacent edges for dequeued item
                adjacent_edges = self.vertices[dequeuedItem[0]][1]
                # go through all adjacent edges
                for edge in adjacent_edges:
                    # and update the indegree by decrementing by 1
                    self.vertices[edge][0] -= 1
                    # if any of these adjacent vertices now have an indegree of 0
                    if self.vertices[edge][0] == 0:
                        # add then to the queue
                        self.insertAlphabetically((edge, 0))
        return self.result


if __name__ == "__main__":
    solution = Solution1("input.txt").solve()
    print(solution)