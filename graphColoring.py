##### Graph Coloring Welsh Powell #########
# 1 - Order the nodes in descending degree
# 2 - For each node, check the colors of neighbor nodes and mark them as unavailable
# 3 - Choose the lowest available color.


def color_nodes(graph):
    # Order nodes in descending degree
    color_map = {}
    # Consider nodes in descending degree
    for node in sorted(graph, key=lambda x: len(graph[x]), reverse=True):
        neighbor_colors = set(color_map.get(neigh) for neigh in graph[node])
        color_map[node] = next(
            color for color in range(len(graph)) if color not in neighbor_colors
        )
    return color_map

if __name__ == '__main__':
    graph = {
        'A' : ['B','C','D'],
        'B' : ['A', 'C'],
        'C' : ['A','B', 'D', 'E', 'F'],
        'D' : ['A','C','E'],
        'E' : ['C', 'D', 'F'],
        'F' : ['C', 'E']

    }
    print(color_nodes(graph))