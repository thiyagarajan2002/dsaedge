import heapq

class Prim:
    """
    Implementation of Prim's algorithm for finding the Minimum Spanning Tree (MST)
    of a connected, undirected, weighted graph.
    """
    def __init__(self, graph):
        """
        Initializes the Prim object with a graph.

        Args:
            graph (dict): A dictionary representing the graph's adjacency list.
                          Example: {'A': [('B', 2), ('C', 3)], 'B': [('A', 2), ...]}
        """
        self.graph = graph
        self.vertices = list(graph.keys())

    def find_mst(self, start_vertex):
        """
        Calculates the Minimum Spanning Tree (MST) using Prim's algorithm.

        Args:
            start_vertex: The vertex from which to start building the MST.

        Returns:
            tuple: A tuple containing:
                - mst_cost (float): The total cost of the MST.
                - mst_edges (list): A list of tuples representing the edges in the MST.
                                    Example: [('A', 'B', 2), ('B', 'D', 5), ...]
        """
        if start_vertex not in self.vertices:
            raise ValueError("Start vertex not in graph.")

        mst_cost = 0
        mst_edges = []
        visited = {start_vertex}
        # (weight, from_vertex, to_vertex)
        pq = [(weight, start_vertex, neighbor) for neighbor, weight in self.graph.get(start_vertex, [])]
        heapq.heapify(pq)

        while pq and len(visited) < len(self.vertices):
            weight, u, v = heapq.heappop(pq)

            if v not in visited:
                visited.add(v)
                mst_cost += weight
                mst_edges.append((u, v, weight))

                for neighbor, next_weight in self.graph.get(v, []):
                    if neighbor not in visited:
                        heapq.heappush(pq, (next_weight, v, neighbor))

        if len(visited) != len(self.vertices):
            print("Warning: Graph is not connected. The result is a minimum spanning forest.")

        return mst_cost, mst_edges
