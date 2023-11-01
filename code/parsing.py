from graph import Node, Graph


def read(filename):
    with open(filename, 'r') as f:
        return f.read().split()


def open_and_parse(filename):
    data = read(filename)

    n, m, r, s, t, *rest = data
    n = int(n)
    m = int(m)
    r = int(r)

    graph = Graph(s, t)

    offset = 0
    for i in range(n):
        name = rest[i + offset]
        is_red = False

        # TODO: If this crashes at some point, look here
        if rest[i+offset+1] == '*':
            is_red = True
            offset += 1

        node = Node(name, is_red)
        graph.add_node(node)
        if name == s:
            graph.start = node
        elif name == t:
            graph.target = node

    rest = rest[n+offset:]

    for i in range(m):
        x = i * 3

        node1 = graph.get_node(rest[x])
        node2 = graph.get_node(rest[x + 2])
        directed = rest[x + 1] == '->'

        graph.add_edge(node1, node2, directed)

    return graph
