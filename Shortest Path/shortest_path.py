import numpy


# Function to find the shortest path in a graph using Dijkstra's algorithm.
def shortest_path(nodes, start, end):
    distance = [float("inf")] * 5
    previous = [None] * 5
    visited = [False] * 5
    distance[start] = 0
    # Loop through all nodes.
    for _ in range(5):
        min_distance = float("inf")
        current = None
        # Find the node with the smallest distance that has not been visited.
        for n in range(5):
            if distance[n] < min_distance and not visited[n]:
                min_distance = distance[n]
                current = n
        # If no node was found, break the loop.
        if current is None:
            break
        # Mark the current node as visited.
        visited[current] = True
        # Update the distances of the neighboring nodes.
        for n in range(5):
            if nodes[current][n] != 0 and distance[current] + nodes[current][n] < distance[n]:
                distance[n] = distance[current] + nodes[current][n]
                previous[n] = current
    # Start from the end node and trace back the path.
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    # Reverse the path to get the correct order from start to end.
    path.reverse()
    return path


# Main function.
if __name__ == "__main__":
    # Define the graph as a 2D array and a dictionary to map city names to nodes.
    graph = numpy.array([[0, 50, 40, 0, 0], [50, 0, 0, 0, 200], [40, 0, 0, 130, 175], [0, 0, 130, 0, 180],
                         [0, 200, 175, 180, 0]])
    city_dict = {0: "Bend", 1: "Medford", 2: "Klamath Falls", 3: "Reno", 4: "San Fransisco"}

    # Find the shortest path from node 0 to node 4.
    shortest_path = shortest_path(graph, 0, 4)
    # Calculate the total distance of the shortest path.
    total_distance = 0
    for i in range(len(shortest_path) - 1):
        total_distance += graph[shortest_path[i]][shortest_path[i + 1]]
    # Print the shortest path and its distance.
    print(f"Shortest Path: {[city_dict[c] for c in shortest_path]}, Distance: {total_distance}")
