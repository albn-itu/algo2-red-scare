import pytest
from parsing import open_and_parse
from utils import get_path_length
from algorithms import alternating_bfs, ignoring_red_vertices_bfs


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
