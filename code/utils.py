def print_dict(dictionary):
    for key, value in dictionary.items():
        print(f"{str(key)}: {str(value)}")


def get_path_length(graph, parent):
    len = 0
    current = graph.target
    while current in parent:
        current = parent[current]
        len += 1
        if current == graph.start:
            return len
    return -1
