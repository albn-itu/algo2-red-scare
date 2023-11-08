# TODO: Write your algorithm code here. Such as BFS, DFS, A*, Ford-Fulkerson, etc.
from graph import Graph, Node
from collections import deque


def alternating_bfs(graph):
    return bfs_general(
        graph,
        (graph.start, graph.start.is_red),
        get_node=lambda queue_element: queue_element[0],
        should_queue=lambda queue_element, _, node: queue_element[1] != node.is_red,
        to_queue_element=lambda _, node: (node, node.is_red)
    )


def ignoring_red_vertices_bfs(graph):
    return bfs_general(
        graph,
        graph.start,
        should_queue=lambda _, __, node: not node.is_red or node == graph.target
    )


def bfs_general(
    graph,
    initial,
    get_node=lambda queue_element: queue_element,
    should_queue=lambda queue_element, node1, node2: True,
    to_queue_element=lambda queue_element, node: node
):
    visited = set()
    queue = deque()
    parent = dict()

    queue.append(initial)

    while queue:
        queue_element = queue.popleft()
        node = get_node(queue_element)

        for e in graph.neighbours(node):
            if e not in visited and should_queue(queue_element, node, e):
                visited.add(e)
                parent[e] = node
                queue.append(to_queue_element(queue_element, e))

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
