import sys


def parse_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    # Assumption 1: lines are not surrounded with quotes, no empty lines in file
    lines = [line.replace(', ', ',').split(',') for line in lines]
    return lines


def create_graph(initial_data):
    graph = dict()
    for node_a, node_b, distance in initial_data:
        # Assumption 2: distances must be greater than or equal to 0
        distance = int(distance)
        if distance < 0:
            raise ValueError('Negative distances are not allowed.')
        graph.setdefault(node_a, dict()).setdefault(node_b, []).append(distance)
        graph.setdefault(node_b, dict()).setdefault(node_a, []).append(distance)
    return graph


def shortest_path(graph, start, end):
    if graph.get(start, None) is None:
        raise KeyError(start)
    if graph.get(end, None) is None:
        raise KeyError(end)

    queue = [{'path': [start], 'length': 0}]
    extended_nodes = []

    while len(queue):
        path_to_extend = queue.pop(0)

        node = path_to_extend['path'][-1]
        if node == end:
            return path_to_extend

        extended_nodes.append(node)
        for next_node, distances in graph[node].items():
            if next_node not in extended_nodes:
                queue.append({
                    'path': path_to_extend['path'] + [next_node],
                    'length': path_to_extend['length'] + min(distances)
                })
        queue = sorted(queue, key=lambda path: path['length'])

    return None


def distance(initial_data, node_a, node_b):
    graph = create_graph(initial_data)

    try:
        return shortest_path(graph, node_a, node_b)
    except KeyError as e:
        raise Exception('There is no node named %s' % e)


if __name__ == "__main__":
    filename, node_a, node_b = sys.argv[1:]
    initial_data = parse_file(filename)
    try:
        print('The shortest path from {0} to {1} is {2}'.format(node_a, node_b, distance(initial_data, node_a, node_b)))
    except Exception as e:
        print(e)
