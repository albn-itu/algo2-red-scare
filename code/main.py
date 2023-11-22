import os
import sys
import parsing
from argparse import ArgumentParser
from algorithms import alternating_bfs, ignoring_red_vertices_bfs, topological_sort, longest_chain, DFS_find_all_paths, dijkstra
from copy import deepcopy
from utils import get_path_length, val_or_na, write_results


def none(graph):
    parent = ignoring_red_vertices_bfs(graph)
    return get_path_length(graph, parent)


def some(graph, many_res, few_res):

    if (many_res > 0 or few_res > 0):
        return True
    elif (many_res == 0):
        return False
    else:
        return DFS_find_all_paths(graph)


def few(graph):
    dist, _ = dijkstra(graph)
    if dist[graph.target] == sys.maxsize:
        return -1
    return dist[graph.target]


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
    n = none(deepcopy(graph))
    f = few(deepcopy(graph))
    m = many(deepcopy(graph))
    s = some(deepcopy(graph), m, f)
    a = alternate(deepcopy(graph))

    return [graph.name, graph.n, 
            val_or_na(a), 
            val_or_na(f), 
            val_or_na(m), 
            val_or_na(n), 
            val_or_na(s)]


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
    parser.add_argument('-f', '--file', default='data/G-ex.txt',
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
