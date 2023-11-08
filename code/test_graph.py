from parsing import parse


def test_contains_cycle_small():
    data = [
        "3", "3", "0", "0", "2",  # n,m,r,s,t
        "0", "1", "2",  # vertex
        "0", "->", "1",  # edge
        "1", "->", "2",  # edge
        "2", "->", "0",  # edge
    ]

    graph = parse(data)
    assert graph.contains_cycle()


def test_contains_cycle_bigger():
    data = [
        "6", "6", "0", "A", "F",  # n,m,r,s,t
        "A", "B", "C", "D", "E", "F",  # vertex
        "A", "->", "B",  # edge
        "B", "->", "C",  # edge
        "C", "->", "E",  # edge
        "E", "->", "F",  # edge
        "E", "->", "D",  # edge
        "D", "->", "B",  # edge
    ]

    graph = parse(data)
    assert graph.contains_cycle()


def test_does_not_contain_cycle_small():
    data = [
        "3", "3", "0", "0", "2",  # n,m,r,s,t
        "0", "1", "2",  # vertex
        "0", "->", "1",  # edge
        "0", "->", "2",  # edge
        "1", "->", "2",  # edge
    ]

    graph = parse(data)
    assert not graph.contains_cycle()
