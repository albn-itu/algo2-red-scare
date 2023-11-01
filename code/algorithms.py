# TODO: Write your algorithm code here. Such as BFS, DFS, A*, Ford-Fulkerson, etc.

def BFS_ignoring_red_vertices(graph) :
    queue = [] 
    parent = dict()
    explored = []

    explored.append(graph.start)
    queue.append(graph.start)
    while(len(queue) != 0) :
        v = queue.pop(0)
        if(v == graph.target) :
            return parent
        for e in graph.edges[v] :
            if not e in explored:
                if not e.is_red or e == graph.target :
                    explored.append(e)
                    parent[e] = v
                    queue.append(e)
    return parent