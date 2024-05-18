import numpy
import matplotlib.pyplot as plt


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


# Function to plot the points and paths of the graph.
def plot():
    # Define the coordinates for each city.
    plot_dict = {"Bend": (2.7, 12), "Medford": (1, 9), "Klamath Falls": (4, 9), "Reno": (8, 5), "San Fransisco": (3, 1)}

    # Set up the plot.
    plt.figure(figsize=(7, 8))
    plt.axis("off")
    plt.title("Shortest Path From Bend to San Fransisco\n", fontsize=16, weight="bold")
    plt.text(4.5, -.5, f"\nShortest Path: {shortest_path}. Distance: {total_distance}", ha="center", size=12)

    # Draw the arrows for each path and annotate with the distance.
    # The color of the arrow is green if the path is part of the shortest path, otherwise it is black.
    shortest_paths = shortest_path.replace(",", "_").replace(" ", "").lower()
    if "bend_medford" in shortest_paths:
        plt.arrow(2.7, 12, 1-2.7, 9-12, width=0.02, color="mediumseagreen")
    else:
        plt.arrow(2.7, 12, 1-2.7, 9-12, width=0.02)
    plt.annotate("50", (1.6, 10.7))
    if "bend_klamathfalls" in shortest_paths:
        plt.arrow(2.7, 12, 4-2.7, 9-12, width=0.02, color="mediumseagreen")
    else:
        plt.arrow(2.7, 12, 4-2.7, 9-12, width=0.02)
    plt.annotate("40", (3.4, 10.7))
    if "medford_sanfransisco" in shortest_paths:
        plt.arrow(1, 9, 3-1, 1-9, width=0.02, color="mediumseagreen")
    else:
        plt.arrow(1, 9, 3-1, 1-9, width=0.02)
    plt.annotate("200", (1.5, 4.9))
    if "klamathfalls_sanfransisco" in shortest_paths:
        plt.arrow(4, 9, 3-4, 1-9, width=0.02, color="mediumseagreen")
    else:
        plt.arrow(4, 9, 3-4, 1-9, width=0.02)
    plt.annotate("175", (3.6, 4.9))
    if "klamathfalls_reno" in shortest_paths:
        plt.arrow(4, 9, 8-4, 5-9, width=0.02, color="mediumseagreen")
    else:
        plt.arrow(4, 9, 8-4, 5-9, width=0.02)
    plt.annotate("130", (6, 7.1))
    if "reno_sanfransisco" in shortest_paths:
        plt.arrow(8, 5, 3-8, 1-5, width=0.02, color="mediumseagreen")
    else:
        plt.arrow(8, 5, 3-8, 1-5, width=0.02)
    plt.annotate("180", (5.6, 2.7))

    # Draw the dots for each city and annotate with the city name.
    for c in plot_dict:
        (x, y) = plot_dict.get(c)
        # The cities in the shortest path are marked with green dots, otherwise they are black.
        if c in shortest_path:
            plt.scatter(x, y, s=100, color="mediumseagreen")
        else:
            plt.scatter(x, y, s=100, color="black")
        plt.text(x=x+.16, y=y-.11, s=c)
    plt.show()


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
    shortest_path = ", ".join([city_dict[c] for c in shortest_path])
    print(f"Shortest Path: {shortest_path}. Distance: {total_distance}")
    # Plot the graph and the shortest path.
    plot()
