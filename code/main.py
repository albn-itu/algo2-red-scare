import parsing
from argparse import ArgumentParser
from algorithms import alternating_bfs
from utils import print_dict
from copy import deepcopy


def none():
    pass


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
    print(graph)

    print("alternate", alternate(deepcopy(graph)))
