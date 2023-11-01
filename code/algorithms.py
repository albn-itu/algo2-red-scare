# TODO: Write your algorithm code here. Such as BFS, DFS, A*, Ford-Fulkerson, etc.
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
