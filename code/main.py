import parsing
from argparse import ArgumentParser
from algorithms import alternating_bfs, BFS_ignoring_red_vertices
from copy import deepcopy


def none(graph):
    parent = BFS_ignoring_red_vertices(graph)
    len = 0
    current = graph.target
    while current in parent:
        current = parent[current]
        len += 1
        if current == graph.start:
            return len
    return -1


def some():
    pass


def few():
    pass


def many():
    pass


def alternate(graph):
    alternate_res = alternating_bfs(graph)
    if graph.target in alternate_res and alternate_res[graph.target] != 0:
        return 'true'
    else:
        return 'false'


if __name__ == '__main__':
    parser = ArgumentParser(description='Red scare')
    parser.add_argument('-f', '--file', default='../data/G-ex.txt',
                        required=False, help='The file to be parsed')
    args = parser.parse_args()

    # TODO: Hail mary argument that just runs all the files
    # TODO: Run the methods here:
    graph = parsing.open_and_parse(args.file)

    print("alternate", alternate(deepcopy(graph)))
    print("none", none(deepcopy(graph)))
    print(graph.contains_cycle())
