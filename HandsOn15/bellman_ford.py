def bellman_ford(graph, start):
    # Step 1: Initialize distances with infinity for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Step 2: Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Step 3: Check for negative-weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances


# Test case
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

start_node = 'A'
try:
    distances = bellman_ford(graph, start_node)
    print("Shortest distances from node", start_node, ":")
    for node, distance in distances.items():
        print("To node", node, ":", distance)
except ValueError as e:
    print(e)
