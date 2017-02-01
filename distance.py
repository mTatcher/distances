import sys
import networkx as nx


def _parse_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    # Assumption 1: lines are not surrounded with quotes, no empty lines in file
    lines = [line.replace(', ', ',').split(',') for line in lines]
    return lines


def distance(initial_data, city_a, city_b):
    graph = nx.Graph()

    for line in initial_data:
        graph.add_edge(line[0], line[1], weight=int(line[2]))

    # Assumption 2: graph is connected (there is a path from any node to any other)
    if not nx.is_connected(graph):
        raise Exception('The graph must be connected')
    try:
        shortest_path = nx.shortest_path(graph, city_a, city_b, 'weight')
    except KeyError as e:
        raise Exception('There is no node named %s' % e)

    # Could use a list comprehension here, but it lacks readability
    lengths = []
    for i in range(len(shortest_path) - 1):
        lengths.append(graph.get_edge_data(shortest_path[i], shortest_path[i+1])['weight'])
    shortest_path_length = sum(lengths)

    equal_parts = nx.kernighan_lin_bisection(graph)
    cut_size = nx.cut_size(graph, *equal_parts)

    return {
        'shortest path': shortest_path,
        'shortest path length': shortest_path_length,
        'cut size': cut_size
    }


if __name__ == "__main__":
    filename, city_a, city_b = sys.argv[1:]
    initial_data = _parse_file(filename)
    try:
        print(distance(initial_data, city_a, city_b))
    except Exception as e:
        print(e)
