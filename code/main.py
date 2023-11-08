import parsing
from argparse import ArgumentParser
from algorithms import alternating_bfs, ignoring_red_vertices_bfs
from copy import deepcopy
from utils import get_path_length, print_dict


def none(graph):
    parent = ignoring_red_vertices_bfs(graph)
    return get_path_length(graph, parent)


def some():
    pass


def few():
    pass


def many(g):
    algorithms.topological_sort(g)


def alternate(graph):
    parent = alternating_bfs(graph)
    length = get_path_length(graph, parent)
    if length != -1:
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
