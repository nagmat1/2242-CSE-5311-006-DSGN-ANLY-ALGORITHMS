def floyd_warshall(graph):
    # Initialize the distance matrix with the graph's adjacency matrix
    distance = {v1: {v2: float('inf') if v1 != v2 else 0 for v2 in graph} for v1 in graph}
    for v1 in graph:
        for v2 in graph[v1]:
            distance[v1][v2] = graph[v1][v2]

    # Floyd-Warshall algorithm
    for k in graph:
        for i in graph:
            for j in graph:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

# Test case
graph = {
    'A': {'A': 0, 'B': 3, 'C': 6, 'D': 15},
    'B': {'A': float('inf'), 'B': 0, 'C': -2, 'D': float('inf')},
    'C': {'A': float('inf'), 'B': float('inf'), 'C': 0, 'D': 2},
    'D': {'A': float('inf'), 'B': 1, 'C': float('inf'), 'D': 0}
}

distances = floyd_warshall(graph)
print("Shortest distances between all pairs of vertices:")
for v1 in distances:
    for v2 in distances[v1]:
        print(f"From {v1} to {v2}: {distances[v1][v2]}")
