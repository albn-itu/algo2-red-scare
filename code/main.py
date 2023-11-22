import os
import sys
import parsing
from argparse import ArgumentParser
from algorithms import alternating_bfs, ignoring_red_vertices_bfs, topological_sort, longest_chain, dfs_find_all_paths, dijkstra
from copy import deepcopy
from utils import get_path_length, val_or_na, val_to_str, write_results
from datetime import datetime


def none(graph):
    parent = ignoring_red_vertices_bfs(graph)
    return get_path_length(graph, parent)


def some(graph):
    ans = many(graph)

    if (ans > 0):
        return True
    elif (ans == 0):
        return False
    elif graph.contains_cycle():
        return -1
    else:
        return dfs_find_all_paths(graph)


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
    return length != -1


def run(graph):
    print("{} - alternate".format(datetime.now().strftime("%H:%M:%S")))
    a = val_or_na(alternate(deepcopy(graph)))

    print("{} - few".format(datetime.now().strftime("%H:%M:%S")))
    f = val_or_na(few(deepcopy(graph)))

    print("{} - many".format(datetime.now().strftime("%H:%M:%S")))
    m = val_or_na(many(deepcopy(graph)))

    print("{} - none".format(datetime.now().strftime("%H:%M:%S")))
    n = val_or_na(none(deepcopy(graph)))

    print("{} - some".format(datetime.now().strftime("%H:%M:%S")))
    s = val_or_na(some(deepcopy(graph)))

    return [
        graph.name,
        val_to_str(graph.n),
        val_to_str(a),
        val_to_str(f),
        val_to_str(m),
        val_to_str(n),
        val_to_str(s),
    ]


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
