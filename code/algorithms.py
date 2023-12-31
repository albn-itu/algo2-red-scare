# TODO: Write your algorithm code here. Such as BFS, DFS, A*, Ford-Fulkerson, etc.
from graph import Graph, Node
from collections import deque, defaultdict
import heapq
import sys
from dataclasses import dataclass, field
from typing import Any


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

    def dfs(graph: Graph, start: Node, visited, sorted_nodes):
        """
        Performs depth first search on a graph
        """

        stack = []

        stack.append((start, False))

        while len(stack):
            current, is_back = stack.pop()

            if is_back:
                sorted_nodes.append(current)
                continue

            visited.add(current)
            stack.append((current, True))  # Add trace back
            stack.append((current, True))  # Add trace back

            for neighbor in graph.neighbours(current):
                if neighbor not in visited:
                    stack.append((neighbor, False))

    visited = set()
    sorted_nodes = []

    dfs(graph, graph.start, visited, sorted_nodes)
    contains_path_to_target = graph.target in visited

    return sorted_nodes, contains_path_to_target

def longest_chain(g, sorted_nodes):
    dist = defaultdict(lambda: -1)
    dist[sorted_nodes[-1]] = 0

    while sorted_nodes:
        node = sorted_nodes.pop()

        a = 1 if node.is_red else 0

        if dist[node] != -1:
            for neighbor in g.neighbours(node):
                if dist[neighbor] < dist[node] + a:
                    dist[neighbor] = dist[node] + a

    return dist[g.target]


def shortest_chain(g, sorted_nodes):
    dist = defaultdict(lambda: -1)
    dist[sorted_nodes[-1]] = 0
    min_dist = sys.maxsize+1

    while sorted_nodes:
        node = sorted_nodes.pop()

        a = 1 if node.is_red else 0

        if dist[node] != -1:
            for neighbor in g.neighbours(node):
                if dist[neighbor] < dist[node] + a:
                    dist[neighbor] = dist[node] + a

                    if dist[neighbor] < min_dist:
                        min_dist = dist[neighbor]

    return -1 if min_dist >= sys.maxsize else min_dist


def dfs_find_all_paths(graph):
    def dfs(graph: Graph, start: Node):
        """
        Performs depth first search on a graph 
        """

        stack = []
        visited = []
        current_path = []
        nodes_with_path_to_goal = set()
        redCount = 0

        stack.append((start, False))

        while len(stack):
            current, is_back = stack.pop()

            if is_back:
                current_path.pop()
                if current.is_red:
                    redCount -= 1
                continue
            elif (current == graph.target):
                if (redCount > 0 or current.is_red):
                    return True
                else:
                    for v in current_path:
                        nodes_with_path_to_goal.add(v)
                    continue

            visited.append(current)
            current_path.append(current)
            stack.append((current, True))  # Add trace back
            if current.is_red:
                redCount += 1

            for neighbor in graph.neighbours(current):
                if neighbor in nodes_with_path_to_goal and redCount > 0:
                    return True
                elif neighbor not in visited:
                    stack.append((neighbor, False))

        return False

    return dfs(graph, graph.start)


def dijkstra(graph):
    @dataclass(order=True)
    class PrioritizedItem:
        priority: int
        item: Any = field(compare=False)

        def __iter__(self):
            return iter((self.priority, self.item))

    dist = defaultdict(lambda: sys.maxsize)
    parent = defaultdict(lambda: None)
    queue = [PrioritizedItem(0, graph.start)]

    dist[graph.start] = 0

    while queue:
        cur_dist, cur_vertex = heapq.heappop(queue)

        if cur_dist > dist[cur_vertex]:
            continue

        for v in graph.neighbours(cur_vertex):
            new_dist = cur_dist + graph.edge(cur_vertex, v)

            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = cur_vertex
                heapq.heappush(queue, PrioritizedItem(new_dist, v))

    return dist, parent
