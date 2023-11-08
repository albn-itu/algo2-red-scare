import os
import parsing
from argparse import ArgumentParser
from algorithms import alternating_bfs, ignoring_red_vertices_bfs, topological_sort, longest_chain, shortest_chain
from copy import deepcopy
from utils import get_path_length, val_or_na, write_results


def none(graph):
    parent = ignoring_red_vertices_bfs(graph)
    return get_path_length(graph, parent)


def some(graph):
    ans = many(graph)

    if (ans == -1 or ans == 0):
        return False
    else:
        return True


def few(graph):
    # Not possible to run many with topological sort when graph has a cycle
    if graph.is_directed() and not graph.contains_cycle():
        sorted_nodes = topological_sort(graph)
        path = shortest_chain(graph, sorted_nodes)

        return path
    else:
        return -1


def many(graph):
    # Not possible to run many with topological sort when graph has a cycle
    if graph.is_directed() and not graph.contains_cycle():
        sorted_nodes = topological_sort(graph)
        path = longest_chain(graph, sorted_nodes)

        return path
    else:
        return -1


def alternate(graph):
    parent = alternating_bfs(graph)
    length = get_path_length(graph, parent)
    if length != -1:
        return 'true'
    else:
        return 'false'


def run(graph):
    a = val_or_na(alternate(deepcopy(graph)))
    f = val_or_na(few(deepcopy(graph)))
    m = val_or_na(many(deepcopy(graph)))
    n = val_or_na(none(deepcopy(graph)))
    s = val_or_na(some(deepcopy(graph)))

    return [graph.name, graph.n, a, f, m, n, s]


def gather_results():
    files = os.listdir('../data')
    ignored = set(["README.md"])
    results = []

    for i, file in enumerate(files):
        print(f"Running {i+1}/{len(files)} ({file})")

        if file in ignored:
            continue

        graph = parsing.open_and_parse('../data/' + file)
        results.append(run(graph))

    return results


if __name__ == '__main__':
    parser = ArgumentParser(description='Red scare')
    parser.add_argument('-f', '--file', default='../data/G-ex.txt',
                        required=False, help='The file to be parsed')
    parser.add_argument('-a', '--all', action='store_true',)
    args = parser.parse_args()

    if args.all:
        results = gather_results()
        write_results(results)
    else:
        graph = parsing.open_and_parse(args.file)
        res = run(graph)

        print(f"name:\t{res[0]}")
        print(f"n:\t{res[1]}")
        print(f"Alt:\t{res[2]}")
        print(f"Few:\t{res[3]}")
        print(f"Man:\t{res[4]}")
        print(f"Non:\t{res[5]}")
        print(f"Som:\t{res[6]}")
