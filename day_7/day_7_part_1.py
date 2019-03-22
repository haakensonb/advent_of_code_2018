"""
    Advent of Code Day 7
    Part 1
"""
import string


class Graph():
    # constructor
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        # number of steps doesn't have a value until parse_input is called
        self.num_of_steps = None
        self.visited = []
        self.stack = []
        self.vertices = {}
        self.starting_vertices = None
        self.alphabet = string.ascii_uppercase
        self.parse_input(self.input_file_name)


    def parse_input(self, input_file_name):
        possible_steps = set(list(string.ascii_uppercase))
        # possible_steps = set(list("ABCDEF"))
        required_steps = set()

        self.num_of_steps = len(possible_steps)

        self.visited = [False] * self.num_of_steps

        with open(input_file_name) as f:
            for line in f:
                first_letter = line.strip()[5]
                second_letter = line.strip()[-12]
                
                if first_letter not in self.vertices:
                    self.vertices[first_letter] = [second_letter]
                elif first_letter in self.vertices:
                    self.vertices[first_letter].append(second_letter)
                    # make sure that they are in alphabetical order
                    # not the most efficient way
                    self.vertices[first_letter] = sorted(self.vertices[first_letter], reverse=True)
                
                required_steps.add(second_letter)
        
        self.starting_vertices = list(possible_steps - required_steps)
        # self.starting_vertices = sorted(self.starting_vertices, reverse=True)


    def solve(self, current_vertex):
        # vertex_index = 'ABCDEF'.index(current_vertex)
        vertex_index = self.alphabet.index(current_vertex)
        self.visited[vertex_index] = True
        if current_vertex in self.vertices:
            for vertex in self.vertices[current_vertex]:
                # adj_vertex_id = 'ABCDEF'.index(vertex)
                adj_vertex_id = self.alphabet.index(vertex)
                if self.visited[adj_vertex_id] == False:
                    self.solve(vertex)

        self.stack.insert(0, current_vertex)




if __name__ == "__main__":
    # day_7 = Graph("test_input.txt")

    day_7 = Graph("input.txt")
    # print(day_7.vertices)
    # print(day_7.visited)
    # print(day_7.starting_vertices)

    # start = day_7.starting_vertices.pop()
    # day_7.solve(start)

    for vertex in day_7.starting_vertices[::-1]:
        day_7.solve(vertex)


    print(''.join(day_7.stack))
