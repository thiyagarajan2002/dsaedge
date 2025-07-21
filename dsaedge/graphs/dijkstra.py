import heapq

class Dijkstra:
    """
    Implementation of Dijkstra's algorithm for finding the shortest paths
    from a single source to all other vertices in a weighted graph.
    """
    def __init__(self, graph):
        """
        Initializes the Dijkstra object with a graph.

        Args:
            graph (dict): A dictionary representing the graph's adjacency list.
                          Example: {'A': [('B', 1), ('C', 4)], 'B': [('A', 1), ...]}
        """
        self.graph = graph
        self.vertices = list(graph.keys())

    def find_shortest_paths(self, start_vertex):
        """
        Calculates the shortest paths from a given start vertex.

        Args:
            start_vertex: The vertex from which to start the search.

        Returns:
            tuple: A tuple containing:
                - distances (dict): A dictionary of the shortest distances from the start vertex.
                - predecessors (dict): A dictionary of predecessors for path reconstruction.
        """
        if start_vertex not in self.vertices:
            raise ValueError("Start vertex not in graph.")

        distances = {vertex: float('infinity') for vertex in self.vertices}
        predecessors = {vertex: None for vertex in self.vertices}
        distances[start_vertex] = 0
        pq = [(0, start_vertex)]  # (distance, vertex)

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph.get(current_vertex, []):
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))

        return distances, predecessors
