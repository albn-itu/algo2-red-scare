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

    def neighbors(self, node):
        return self.edges[node]

    def get_edges(self, name):
        return self.edges[self.get_node(name)]

    def add_node(self, node):
        self.nodes[node.name] = node
        self.edges[node] = []

    def add_edge(self, node1, node2, directed=False):
        """
        Adds edge between the two nodes. If it is not directed then a reverse edge is being added as well
        """
        self.edges[node1].append(node2)

        if not directed:
            self.edges[node2].append(node1)

    def contains_cycle(self):
        visited = {k: False for k in self.nodes}
        recursion = {k: False for k in self.nodes}

        for vertex, n in self.nodes.items():
            if visited[vertex] == False:
                if self.__isCyclic(vertex, visited, recursion) == True:
                    return True

        return False

    def __isCyclic(self, start_vertex: str, visited, recursion):

        # Create stack and add adjacent vertices of vertice
        stack = deque()
        stack.append((start_vertex, False))

        while stack:
            current_vertex, reset_recursion_flag = stack.pop()

            if reset_recursion_flag:
                recursion[current_vertex] = False
            else:

                if visited[current_vertex] == False:
                    visited[current_vertex] = True
                    recursion[current_vertex] = True
                    stack.append((current_vertex, True))

                    for adjacent_node in self.get_edges(current_vertex):
                        stack.append((adjacent_node.name, False))
                elif recursion[current_vertex] == True:
                    return True

        recursion[start_vertex] = False
        return False

    def __str__(self):
        def edges_str(edges):
            return ', '.join([str(edge) for edge in edges])
        nodes = ', '.join([str(node) for node in self.nodes.values()])
        edges = ', '.join([f"{node}: {{{edges_str(edges)}}}" for node,
                          edges in self.edges.items()])
        return f"Graph(Nodes: [{nodes}], Edges: [{edges}])"
