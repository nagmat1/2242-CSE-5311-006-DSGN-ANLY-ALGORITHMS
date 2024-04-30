import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to store nodes with their current distances from the start node
    pq = [(0, start)]

    while pq:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(pq)

        # Skip this node if we have already found a shorter path to it
        if current_distance > distances[current_node]:
            continue

        # Iterate over neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If the distance to this neighbor through the current node is shorter than the current best distance,
            # update the distance and add the neighbor to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Test case
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'C': 2, 'D': 1},
    'C': {'B': 1, 'D': 4, 'E': 6},
    'D': {'E': 2},
    'E': {}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node, ":")
for node, distance in distances.items():
    print("To node", node, ":", distance)
