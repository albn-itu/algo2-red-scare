# TODO: Write your algorithm code here. Such as BFS, DFS, A*, Ford-Fulkerson, etc.
from graph import Graph, Node

def BFS_ignoring_red_vertices(graph) :
    queue = [] 
    parent = dict()
    explored = []

    explored.append(graph.start)
    queue.append(graph.start)
    while(len(queue) != 0) :
        v = queue.pop(0)
        if(v == graph.target) :
            return parent
        for e in graph.edges[v] :
            if not e in explored:
                if not e.is_red or e == graph.target :
                    explored.append(e)
                    parent[e] = v
                    queue.append(e)
    return parent

def topological_sort(graph: Graph):
    """
    Sorts the graph in a topological order

    Returns: a list with the nodes in topological order
    """

    def dfs(graph: Graph, visited, sorted_nodes):
        """
        Performs depth first search on a graph 
        """

        stack = []

        stack.append((graph.start, False))

        while len(stack):
            current, is_back = stack.pop()

            if is_back:
                sorted_nodes.append(current)
                continue

            visited.add(current)
            stack.append((current, True)) # Add trace back

            for neighbor in graph.nodes[current]:
                if neighbor not in visited:
                    stack.append((neighbor, False))

    visited = set()
    sorted_nodes = []

    for node in graph.nodes:
        if node not in visited:
            dfs(graph, node, visited, sorted_nodes)

    return sorted_nodes

def longest_chain(n, nodes, sorted_nodes):
    dist = [-1] * (n + 1)
    dist[sorted_nodes[-1]] = 0
    max_dist = -1

    while sorted_nodes:
        node = sorted_nodes.pop()

        if dist[node] != -1:
            for neighbor in nodes[node]:
                if dist[neighbor] < dist[node] + 1:
                    dist[neighbor] = dist[node] + 1

                    if dist[neighbor] > max_dist:
                        max_dist = dist[neighbor]

    return max_dist
