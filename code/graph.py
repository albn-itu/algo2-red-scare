from functools import cached_property
from typing import Dict
from collections import deque


class Node():
    def __init__(self, name: str, is_red: bool):
        self.name = name
        self.is_red = is_red

    def __str__(self):
        return f"Node({self.name}, {self.is_red})"

    def __repr__(self):
        return str(self)
    # TODO: Implement hash and equality. This may be needed for the graph later


class Graph():
    def __init__(self, n: int, start: Node, target: Node):
        self.name = "unnamed"
        self.n = n

        self.__nodes = dict()  # string -> Node
        self.__edges = dict()  # Node -> Node -> int

        self.start = start
        self.target = target
        self.directed = True

    def set_name(self, name: str):
        if name.endswith(".txt"):
            import os
            name = os.path.splitext(os.path.basename(name))[0]

        self.name = name

    def get_node(self, name: str):
        return self.__nodes[name]

    def nodes(self):
        return self.__nodes.values()

    def edges(self):
        return self.__edges

    def edge(self, node1: Node, node2: Node):
        return self.__edges[node1][node2]

    def neighbours(self, node: Node):
        return list(self.__edges[node].keys())

    def add_node(self, node: Node):
        self.__nodes[node.name] = node
        self.__edges[node] = dict()

    def add_edge(self, node1: Node, node2: Node, directed=False):
        """
        Adds edge between the two nodes.
        If it is not directed then a reverse edge is being added as well
        """
        self.__edges[node1][node2] = 1 if node2.is_red else 0

        if not directed:
            self.directed = False
            self.__edges[node2][node1] = 1 if node1.is_red else 0

    def is_directed(self):
        return self.directed

    @cached_property
    def contains_cycle(self):
        visited = {k: False for k in self.__nodes.values()}
        recursion = {k: False for k in self.__nodes.values()}

        for n in self.__nodes.values():
            if not visited[n]:
                if self.__isCyclic(n, visited, recursion):
                    return True

        return False

    def __isCyclic(
        self,
        start_vertex: Node,
        visited: Dict[Node, bool],
        recursion: Dict[Node, bool]
    ):
        # Create stack and add adjacent vertices of vertice
        stack = deque()
        stack.append((start_vertex, False))

        while stack:
            current_vertex, reset_recursion_flag = stack.pop()

            if reset_recursion_flag:
                recursion[current_vertex] = False
            else:

                if not visited[current_vertex]:
                    visited[current_vertex] = True
                    recursion[current_vertex] = True
                    stack.append((current_vertex, True))

                    for adjacent_node in self.neighbours(current_vertex):
                        stack.append((adjacent_node, False))
                elif recursion[current_vertex]:
                    return True

        recursion[start_vertex] = False
        return False

    def __str__(self):
        def edges_str(edges):
            return ', '.join([str(edge) for edge in edges])
        nodes = ', '.join([str(node) for node in self.__nodes.values()])
        edges = ', '.join([f"{node}: {{{edges_str(edges)}}}" for node,
                          edges in self.__edges.items()])
        return f"Graph(Nodes: [{nodes}], Edges: [{edges}])"
