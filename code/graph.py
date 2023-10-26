class Node():
    def __init__(self, name, is_red):
        self.name = name
        self.is_red = is_red

    def __str__(self):
        return f"Node({self.name}, {self.is_red})"


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

    def __str__(self):
        def edges_str(edges):
            return ', '.join([str(edge) for edge in edges])
        nodes = ', '.join([str(node) for node in self.nodes.values()])
        edges = ', '.join([f"{node}: {{{edges_str(edges)}}}" for node,
                          edges in self.edges.items()])
        return f"Graph(Nodes: [{nodes}], Edges: [{edges}])"
