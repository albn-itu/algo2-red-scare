import parsing
from argparse import ArgumentParser
import algorithms


def none():
    pass


def some():
    pass


def few():
    pass


def many():
    pass


def alternate():
    pass


if __name__ == '__main__':
    parser = ArgumentParser(description='Red scare')
    parser.add_argument('-f', '--file', default='../data/G-ex.txt',
                        required=False, help='The file to be parsed')
    args = parser.parse_args()

    # TODO: Hail mary argument that just runs all the files
    # TODO: Parsing
    # TODO: Run the methods here:
    graph = parsing.open_and_parse(args.file)
    print(graph)
