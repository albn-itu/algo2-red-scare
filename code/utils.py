from print_graph import create_output_folder


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


def val_or_na(val):
    return val if val is not None else "NA"


def val_to_str(val):
    if isinstance(val, str):
        return val
    elif isinstance(val, bool):
        return "true" if val else "false"
    elif isinstance(val, int):
        if val == -2:
            return '?!'
        return str(val)


def write_txt_results(results):
    with open('graph-output/results.txt', 'w') as f:
        results = [["instance", "n", "A", "F", "M", "N",
                    "S", "At", "Ft", "Mt", "Nt", "St"]] + results

        for res in results:
            f.write("{}\n".format("\t".join([str(x) for x in res])))


def write_tex_results(results, filename='results'):
    start = """
\\medskip
\\begin{longtable}{lrrrrrrrrrrr}
\\toprule
\tInstance name & $n$ & A & F & M & N & S\\\\
\t\\midrule
"""
    end = """
\t\\bottomrule
\\end{longtable}
\\medskip
"""

    with open(f'graph-output/{filename}.tex', 'w') as f:
        f.write(start)
        for res in results:
            f.write("\t{}\\\\\n".format(" & ".join([str(x) for x in res[:7]])))
        f.write(end)


def write_results(results):
    create_output_folder()

    results = sorted(results, key=lambda x: x[0])

    write_txt_results(results)
    write_tex_results(results)

    smallResults = [res for res in results if int(res[1]) >= 500]
    write_tex_results(smallResults, filename='results-large')
