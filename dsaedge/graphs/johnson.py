from .bellman_ford import bellman_ford
from .dijkstra import Dijkstra

class Johnson:
    """
    Implementation of Johnson's algorithm for finding all-pairs shortest paths
    in a sparse, weighted, directed graph. It can handle negative edge weights
    but not negative cycles.
    """
    def __init__(self, graph):
        """
        Initializes the Johnson object with a graph.

        Args:
            graph (dict): A dictionary representing the graph's adjacency list.
                          Example: {'A': [('B', -2)], 'B': [('C', -1)], ...}
        """
        self.graph = graph
        self.vertices = list(graph.keys())

    def find_all_pairs_shortest_paths(self):
        """
        Calculates all-pairs shortest paths using Johnson's algorithm.

        Returns:
            dict: A dictionary of dictionaries representing the shortest paths
                  between all pairs of vertices. Example: {'A': {'B': -2, 'C': -3}, ...}
        """
        # 1. Add a new vertex 's' with zero-weight edges to all other vertices.
        temp_graph = self.graph.copy()
        temp_graph['s'] = [(v, 0) for v in self.vertices]

        # 2. Run Bellman-Ford from 's' to find re-weighting values (h).
        # We need a graph representation suitable for the bellman_ford function.
        num_vertices = len(self.vertices) + 1
        vertex_map = {name: i for i, name in enumerate(self.vertices + ['s'])}
        reverse_map = {i: name for name, i in vertex_map.items()}

        bf_graph = type('Graph', (), {'V': num_vertices, 'graph': []})()
        for u, edges in temp_graph.items():
            for v, w in edges:
                bf_graph.graph.append([vertex_map[u], vertex_map[v], w])

        h, _, negative_cycle = bellman_ford(bf_graph, vertex_map['s'])

        if negative_cycle:
            raise ValueError("Graph contains a negative cycle.")

        # 3. Re-weight the original graph.
        reweighted_graph = {u: [] for u in self.vertices}
        for u, edges in self.graph.items():
            for v, w in edges:
                h_u = h[vertex_map[u]]
                h_v = h[vertex_map[v]]
                reweighted_graph[u].append((v, w + h_u - h_v))

        # 4. Run Dijkstra from each vertex on the re-weighted graph.
        all_shortest_paths = {}
        dijkstra_solver = Dijkstra(reweighted_graph)
        for u in self.vertices:
            distances, _ = dijkstra_solver.find_shortest_paths(u)
            # 5. Adjust the distances back.
            adjusted_distances = {}
            for v, dist in distances.items():
                if dist != float('infinity'):
                    h_u = h[vertex_map[u]]
                    h_v = h[vertex_map[v]]
                    adjusted_distances[v] = dist - h_u + h_v
            all_shortest_paths[u] = adjusted_distances

        return all_shortest_paths
