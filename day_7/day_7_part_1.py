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
        self.starting_vertice = None
        self.parse_input(self.input_file_name)


    def parse_input(self, input_file_name):
        # possible_steps = set(list(string.ascii_uppercase))
        possible_steps = set(list("ABCDEF"))
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
                    self.vertices[first_letter] = sorted(self.vertices[first_letter])
                
                required_steps.add(second_letter)
        
        self.starting_vertice = (possible_steps - required_steps).pop()


    def visit(self, current_vertex):
        vertex_index = 'ABCDEF'.index(current_vertex)

        # base case
        if self.visited[vertex_index]:
            return

        self.visited[vertex_index] = True

        if current_vertex in self.vertices:
            for required_vertex in self.vertices[current_vertex]:
                required_vertex_id = 'ABCDEF'.index(required_vertex)
                if not self.visited[required_vertex_id]:
                    self.visit(required_vertex)

        self.stack.append(current_vertex)

    def are_all_visited(self):
        for vertex in self.visited:
            if not vertex:
                return False
        return True


    def solve(self):
        keep_going = True
        while keep_going:
            if self.are_all_visited():
                keep_going = False
            else:
                self.visit(self.starting_vertice)
        print(self.stack)



if __name__ == "__main__":
    day_7 = Graph("test_input.txt")
    print(day_7.vertices)
    print(day_7.visited)
    print(day_7.starting_vertice)
    day_7.solve()
