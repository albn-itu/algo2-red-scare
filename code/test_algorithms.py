import pytest
from parsing import open_and_parse, parse
from utils import get_path_length
from algorithms import alternating_bfs, ignoring_red_vertices_bfs, topological_sort, longest_chain, shortest_chain, dijkstra, dfs_find_all_paths


@pytest.mark.parametrize("test_file,expected_length", [
    ("../data/G-ex.txt", 2),
    ("../data/P3.txt", 2),
    ("./test-data/P3-1.txt", -1),
    ("./test-data/K3-0.txt", 2),
    ("./test-data/K3-1.txt", 2),
    ("./test-data/K3-2.txt", -1),
    ("../data/rusty-1-17.txt", -1),
    ("../data/grid-5-0.txt", 4),
    ("../data/wall-p-1.txt", -1),
    ("../data/wall-p-3.txt", -1),
    ("../data/wall-z-3.txt", -1),
    ("../data/wall-n-2.txt", -1),
    ("../data/increase-n8-1.txt", 1),
    ("../data/increase-n8-2.txt", 1),
])
def test_alternating_bfs(test_file, expected_length):
    graph = open_and_parse(test_file)
    parent = alternating_bfs(graph)

    assert get_path_length(graph, parent) == expected_length


@pytest.mark.parametrize("test_file,expected_length", [
    ("../data/G-ex.txt", 3),
    ("../data/P3.txt", -1),
    ("./test-data/P3-1.txt", 2),
    ("./test-data/K3-0.txt", 1),
    ("./test-data/K3-1.txt", 1),
    ("./test-data/K3-2.txt", 1),
    ("../data/rusty-1-17.txt", 10),
    ("../data/grid-5-0.txt", 14),
    ("../data/wall-p-1.txt", 1),
    ("../data/wall-p-3.txt", 1),
    ("../data/wall-z-3.txt", 1),
    ("../data/wall-n-2.txt", 1),
    ("../data/increase-n8-1.txt", 1),
    ("../data/increase-n8-2.txt", 1),
])
def test_ignoring_red_vertices_bfs(test_file, expected_length):
    graph = open_and_parse(test_file)
    parent = ignoring_red_vertices_bfs(graph)

    assert get_path_length(graph, parent) == expected_length


def test_longest_chain():
    data = [
        "5", "5", "3", "1", "5",  # n,m,r,s,t
        "1", "*", "2", "*", "3", "4", "*", "5",  # vertex
        "1", "->", "2",  # edge
        "1", "->", "3",  # edge
        "2", "->", "4",  # edge
        "3", "->", "5",  # edge
        "4", "->", "5",  # edge
    ]

    graph = parse(data)
    sorted_nodes, _ = topological_sort(graph)
    max_red_path = longest_chain(graph, sorted_nodes)

    assert max_red_path == 3


def test_shortest_chain():
    data = [
        "5", "5", "3", "1", "5",  # n,m,r,s,t
        "1", "*", "2", "*", "3", "4", "*", "5",  # vertex
        "1", "->", "2",  # edge
        "1", "->", "3",  # edge
        "2", "->", "4",  # edge
        "3", "->", "5",  # edge
        "4", "->", "5",  # edge
    ]

    graph = parse(data)
    sorted_nodes, _ = topological_sort(graph)
    min_red_path = shortest_chain(graph, sorted_nodes)

    assert min_red_path == 1


def test_dijkstra_g_ex():
    data = ["8", "9", "3", "0", "3", "0", "1", "2", "3", "4", "*", "5", "*",
            "6", "7", "*", "0", "--", "1", "1", "--",
            "2", "2", "--", "3", "0", "--", "4", "4", "--", "3", "0", "--", "5",
            "5", "--", "6", "6", "--", "7", "7", "--", "3"]

    graph = parse(data)
    dist, parent = dijkstra(graph)

    assert dist[graph.target] == 0


def test_dijkstra_line():
    data = ["4", "3", "4",
            "0", "3",
            "0", "*",
            "1", "*",
            "2", "*",
            "3", "*",
            "0", "--", "1",
            "1", "--", "2",
            "2", "--", "3"]

    graph = parse(data)
    dist, parent = dijkstra(graph)

    assert dist[graph.target] == 3


def test_dijkstra_classic():
    data = ["6", "3", "4",
            "0", "3",
            "0",
            "1",
            "2", "*",
            "3", "*",
            "4",
            "5", "*",
            "0", "--", "1",
            "0", "--", "2",
            "1", "--", "3",
            "2", "--", "4",
            "3", "--", "5",
            "4", "--", "5",
            "1", "--", "4"]

    graph = parse(data)
    dist, parent = dijkstra(graph)

    assert dist[graph.target] == 1


@pytest.mark.parametrize("test_file,expected_result", [
    ("../data/G-ex.txt", True),
    ("../data/P3.txt", True),
    ("./test-data/P3-1.txt", True),
    ("./test-data/K3-0.txt", True),
    ("./test-data/K3-1.txt", True),
    ("./test-data/K3-2.txt", False),
    ("../data/rusty-1-17.txt", True),
    ("../data/grid-5-0.txt", True),
    ("../data/wall-p-1.txt", True),
    ("../data/wall-p-3.txt", False),
    ("../data/wall-z-3.txt", False),
    ("../data/wall-n-2.txt", False),
    ("../data/increase-n8-1.txt", True),
    ("../data/increase-n8-2.txt", True),
])
def test_dfs(test_file, expected_result):
    graph = open_and_parse(test_file)
    result = dfs_find_all_paths(graph)

    assert result == expected_result
