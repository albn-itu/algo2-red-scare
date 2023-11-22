from parsing import read, parse


def test_read_G_ex():
    """Test the read function."""
    data = ["8", "9", "3", "0", "3", "0", "1", "2", "3", "4", "*", "5", "*",
            "6", "7", "*", "0", "--", "1", "1", "--",
            "2", "2", "--", "3", "0", "--", "4", "4", "--", "3", "0", "--", "5",
            "5", "--", "6", "6", "--", "7", "7", "--", "3"]
    assert read("../data/G-ex.txt") == data


def test_parse_undirected_small():
    data = [
        "2", "1", "0", "node1", "node2",  # n,m,r,s,t
        "node1", "node2",  # vertex
        "node1", "--", "node2",  # edge
    ]

    graph = parse(data)
    print(graph.nodes())
    assert len(graph.nodes()) == 2
    assert graph.get_node("node1") != graph.get_node("node2")
    assert graph.get_node("node1") == graph.start
    assert graph.get_node("node2") == graph.target

    assert len(graph.edges()) == 2  # Because each node has an empty edge list
    assert graph.neighbours(graph.get_node("node1")) == [
        graph.get_node("node2")]
    assert graph.neighbours(graph.get_node("node2")) == [
        graph.get_node("node1")]


def test_parse_directed_small():
    data = [
        "2", "1", "0", "node1", "node2",  # n,m,r,s,t
        "node1", "node2",  # vertex
        "node1", "->", "node2",  # edge
    ]

    graph = parse(data)
    assert len(graph.nodes()) == 2
    assert graph.get_node("node1") != graph.get_node("node2")
    assert graph.get_node("node1") == graph.start
    assert graph.get_node("node2") == graph.target

    assert len(graph.edges()) == 2  # Because each node has an empty edge list
    assert graph.neighbours(graph.get_node("node1")) == [
        graph.get_node("node2")]
    assert graph.neighbours(graph.get_node("node2")) == []


def test_parse_directed_slightly_larger():
    data = [
        "3", "2", "0", "node1", "node3",  # n,m,r,s,t
        "node1", "node2", "node3",  # vertex
        "node1", "->", "node2",  # edge
        "node2", "->", "node3",  # edge
    ]

    graph = parse(data)
    assert len(graph.nodes()) == 3
    assert graph.get_node("node1") == graph.start
    assert graph.get_node("node3") == graph.target

    assert len(graph.edges()) == 3  # Because each node has an empty edge list
    assert graph.neighbours(graph.get_node("node1")) == [
        graph.get_node("node2")]
    assert graph.neighbours(graph.get_node("node2")) == [
        graph.get_node("node3")]
    assert graph.neighbours(graph.get_node("node3")) == []
