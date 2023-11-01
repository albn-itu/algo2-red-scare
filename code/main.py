import parsing
from argparse import ArgumentParser
import algorithms


def none(g):
    parent = algorithms.BFS_ignoring_red_vertices(g)
    len = 0
    current = g.target
    while current in parent :
        current = parent[current]
        len+=1
        if current == g.start :
            return len
    return -1

def some():
    pass


def few():
    pass


def many():
    pass


def alternate():
    pass

def print_dict(d) :
    for k,v in d.items() :
        print(str(k), "->", str(v))

if __name__ == '__main__':
    parser = ArgumentParser(description='Red scare')
    parser.add_argument('-f', '--file', default='../data/G-ex.txt',
                        required=False, help='The file to be parsed')
    args = parser.parse_args()

    # TODO: Hail mary argument that just runs all the files
    # TODO: Run the methods here:
    graph = parsing.open_and_parse(args.file)
    print(graph)
    print(none(graph))
