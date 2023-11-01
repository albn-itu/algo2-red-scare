# TODO: Write your algorithm code here. Such as BFS, DFS, A*, Ford-Fulkerson, etc.
from collections import deque


def alternating_bfs(graph):
    visited = set()
    queue = deque()
    queue.append((graph.start, graph.start.is_red, 0))
    path = dict()

    while queue:
        node, is_red, step = queue.popleft()
        is_red = not is_red
        path[node] = min(path.get(node, float('inf')), step)

        for j in graph.neighbors(node):
            if j.is_red == is_red and (j, is_red) not in visited:
                visited.add((j, is_red))
                queue.append((j, is_red, step + 1))

    return path


def BFS_ignoring_red_vertices(graph):
    queue = []
    parent = dict()
    explored = []

    explored.append(graph.start)
    queue.append(graph.start)
    while (len(queue) != 0):
        v = queue.pop(0)
        if (v == graph.target):
            return parent
        for e in graph.edges[v]:
            if not e in explored:
                if not e.is_red or e == graph.target:
                    explored.append(e)
                    parent[e] = v
                    queue.append(e)
    return parent
