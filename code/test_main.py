import pytest
from parsing import open_and_parse
from main import alternate, none


@pytest.mark.parametrize("test_file,expected", [
    ("../data/G-ex.txt", 'true'),
    ("../data/P3.txt", 'true'),
    ("./test-data/P3-1.txt", 'false'),
    ("./test-data/K3-0.txt", 'true'),
    ("./test-data/K3-1.txt", 'true'),
    ("./test-data/K3-2.txt", 'false'),
    ("../data/rusty-1-17.txt", 'false'),
    ("../data/grid-5-0.txt", 'true'),
    ("../data/wall-p-1.txt", 'false'),
    ("../data/wall-p-3.txt", 'false'),
    ("../data/wall-z-3.txt", 'false'),
    ("../data/wall-n-2.txt", 'false'),
    ("../data/increase-n8-1.txt", 'true'),
    ("../data/increase-n8-2.txt", 'true'),
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
