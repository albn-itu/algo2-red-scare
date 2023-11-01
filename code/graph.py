from collections import defaultdict, deque

class Node():
    def __init__(self, name, is_red):
        self.name = name
        self.is_red = is_red

    def __str__(self):
        return f"Node({self.name}, {self.is_red})"

    # TODO: Implement hash and equality. This may be needed for the graph later


class Graph():
    def __init__(self, start, target):
        self.nodes = dict()  # string -> Node
        self.edges = dict()  # Node -> Node[]

        self.start = start
        self.target = target

    def get_node(self, name):
        return self.nodes[name]

    def add_node(self, node):
        self.nodes[node.name] = node
        self.edges[node] = []

    def add_edge(self, node1, node2, directed=False):
        self.edges[node1].append(node2)

        if directed:
            self.edges[node2].append(node1)

    def contains_cycle(self):
        visited = [False] * self.Vertices
        recursion = [False] * self.Vertices

        for vertice in range(self.Vertices):
            if visited[vertice] == False:
                if self.__isCyclic(vertice, visited, recursion) == True:
                    return True
        
        return False
    
    def __isCyclic(self, start_vertice: int, visited, recursion):

        # Create stack and add adjacent vertices of vertice 
        stack = deque()
        stack.append((start_vertice, False))

        while stack:
            current_vertice, reset_recursion_flag = stack.pop()

            if reset_recursion_flag:
                recursion[current_vertice] = False
            else:

                if visited[current_vertice] == False:
                    visited[current_vertice] = True
                    recursion[current_vertice] = True
                    stack.append((current_vertice, True))

                    for adjacent_vertice in self.edges[current_vertice]:
                        stack.append((adjacent_vertice, False))
                elif recursion[current_vertice] == True:
                    return True
            
        recursion[start_vertice] = False
        return False

    def __str__(self):
        def edges_str(edges):
            return ', '.join([str(edge) for edge in edges])
        nodes = ', '.join([str(node) for node in self.nodes.values()])
        edges = ', '.join([f"{node}: {{{edges_str(edges)}}}" for node,
                          edges in self.edges.items()])
        return f"Graph(Nodes: [{nodes}], Edges: [{edges}])"
