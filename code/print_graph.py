# This is a standalone main file that can be run to print the graph
import parsing
from argparse import ArgumentParser
import algorithms


def get_red_fill_style(node, style):
    if node.is_red:
        style['fillcolor'] = 'red'
        style['style'] = 'filled'
        style['fontcolor'] = 'white'
    return style


def get_start_style(node, style):
    style['shape'] = 'Mdiamond'

    return style


def get_target_style(node, style):
    style['shape'] = 'Msquare'

    return style


def create_node_style(style):
    styles = []

    if len(style) == 0:
        return ""

    for key, value in style.items():
        styles.append(f"{key}={value}")

    return "[{0}]".format(','.join(styles))


def get_node(node, is_start, is_target):
    style = dict()
    style = get_red_fill_style(node, style)
    if is_start:
        style = get_start_style(node, style)
    elif is_target:
        style = get_target_style(node, style)

    if len(style) == 0:
        return ""

    return f"   \"{node.name}\" {create_node_style(style)}\n"


def get_edge(node1, node2):
    return f"   \"{node1.name}\" -> \"{node2.name}\"\n"


def create_output_folder():
    import os
    if not os.path.exists('./graph-output'):
        os.makedirs('./graph-output')
        with open('./graph-output/.gitignore', 'w') as f:
            f.write('*')


if __name__ == '__main__':
    parser = ArgumentParser(description='Red scare - print graph')
    parser.add_argument('-f', '--file', default='../data/G-ex.txt',
                        required=False, help='The file to be parsed')
    args = parser.parse_args()

    graph = parsing.open_and_parse(args.file)

    filename = args.file.split('/')[-1].split('.')[0]
    create_output_folder()
    with open(f"./graph-output/{filename}.dot", 'w') as f:
        f.write("digraph \"{0}\" {{\n".format(filename))

        for node in graph.nodes():
            f.write(get_node(node, node == graph.start, node == graph.target))
        for node1 in graph.nodes():
            for node2 in graph.neighbours(node1):
                f.write(get_edge(node1, node2))
        f.write("}")
