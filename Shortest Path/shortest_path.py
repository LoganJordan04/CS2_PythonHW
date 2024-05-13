import numpy


def shortest_path(graph, start, end):
    distance = [float("inf")]*5
    previous = [None]*5
    visited = [False]*5
    distance[start] = 0
    for _ in range(5):
        min_distance = float("inf")
        current = None
        for j in range(5):
            if distance[j] < min_distance and not visited[j]:
                min_distance = distance[j]
                current = j
        if current is None:
            break
        visited[current] = True
        for j in range(5):
            if graph[current][j] != 0 and distance[current] + graph[current][j] < distance[j]:
                distance[j] = distance[current] + graph[current][j]
                previous[j] = current

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path


if __name__ == "__main__":
    graph = numpy.array([[0, 50, 40, 0, 0], [50, 0, 0, 0, 200], [40, 0, 0, 130, 175], [0, 0, 130, 0, 180],
                         [0, 200, 175, 180, 0]])
    city_dict = {0: "Bend", 1: "Medford", 2: "Klamath Falls", 3: "Reno", 4: "San Fransisco"}

    shortest_path = shortest_path(graph, 0, 4)
    distance = 0
    for i in range(len(shortest_path)-1):
        distance += graph[shortest_path[i]][shortest_path[i+1]]
    print(f"Shortest Path: {[city_dict[i] for i in shortest_path]}, Distance: {distance}")
