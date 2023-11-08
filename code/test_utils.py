from parsing import open_and_parse
from utils import get_path_length


def test_path_length_4():
    # start: 0, target: 3
    graph = open_and_parse("../data/G-ex.txt")

    parent = {
        graph.get_node("3"): graph.get_node("7"),
        graph.get_node("7"): graph.get_node("6"),
        graph.get_node("6"): graph.get_node("5"),
        graph.get_node("5"): graph.get_node("0"),
    }

    assert get_path_length(graph, parent) == 4


def test_path_length_2():
    # start: 0, target: 3
    graph = open_and_parse("../data/G-ex.txt")

    parent = {
        graph.get_node("3"): graph.get_node("4"),
        graph.get_node("4"): graph.get_node("0"),
    }

    assert get_path_length(graph, parent) == 2
