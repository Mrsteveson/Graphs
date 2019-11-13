from util import Stack, Queue
# First Pass Attempt
# Shortest Path == Breath-First
# Farthest away ancestor
# Utilizing a Queue and Graph data structure
# BFT/BFS for possible solutions

# Graph from yesterday's material
class Graph:
    def __init__(self):
        self.vertices = {}

    # Overwriting with a new set breaks the tests
    # def add_vertex(self, vertex):
    #     self.vertices[vertex] = set()

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

# Utilize Queue/Graph and BFT/BFS approach to solve.
def earliest_ancestor(ancestors, starting_node):
    # Create the graph
    g = Graph()
    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        # Links from children to parents
        g.add_edge(pair[1], pair[0])
    
    # Setup a BFS
    q = Queue()
    q.enqueue([starting_node])

    # Initialize longest_path and earliest_ancestor
    # Connected by exactly one path
    # If individual has no parents, return -1
    longest_path = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        vertex = path[-1]
        # If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.
        if (len(path) >= longest_path and vertex < earliest_ancestor) or (len(path) > longest_path):
            earliest_ancestor = vertex
            longest_path = len(path)
        for neighbor in g.vertices[vertex]:
            new_path = list(path)
            new_path.append(neighbor)
            q.enqueue(new_path)

    return earliest_ancestor