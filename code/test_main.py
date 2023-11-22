import pytest
from parsing import open_and_parse
from main import alternate, none


@pytest.mark.parametrize("test_file,expected", [
    ("../data/G-ex.txt", True),
    ("../data/P3.txt", True),
    ("./test-data/P3-1.txt", False),
    ("./test-data/K3-0.txt", True),
    ("./test-data/K3-1.txt", True),
    ("./test-data/K3-2.txt", False),
    ("../data/rusty-1-17.txt", False),
    ("../data/grid-5-0.txt", True),
    ("../data/wall-p-1.txt", False),
    ("../data/wall-p-3.txt", False),
    ("../data/wall-z-3.txt", False),
    ("../data/wall-n-2.txt", False),
    ("../data/increase-n8-1.txt", True),
    ("../data/increase-n8-2.txt", True),
])
def test_alternate(test_file, expected):
    graph = open_and_parse(test_file)

    assert alternate(graph) == expected


@pytest.mark.parametrize("test_file,expected", [
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
def test_none(test_file, expected):
    graph = open_and_parse(test_file)

    assert none(graph) == expected
