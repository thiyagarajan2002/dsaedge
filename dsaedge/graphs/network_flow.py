from collections import deque

class NetworkFlow:
    """
    Implements the Edmonds-Karp algorithm to find the maximum flow in a flow network.
    This is a specific implementation of the Ford-Fulkerson method that uses BFS
    to find augmenting paths in the residual graph.
    """
    def __init__(self, graph):
        """
        Initializes the NetworkFlow object.

        Args:
            graph (dict): A dictionary representing the graph's capacity.
                          The keys are vertices, and the values are dictionaries
                          representing the capacities to neighboring vertices.
                          Example: {'s': {'a': 10, 'b': 5}, 'a': {'c': 10}, ...}
        """
        self.graph = graph
        self.vertices = list(graph.keys())
        # The residual graph is initially a copy of the capacity graph.
        self.residual_graph = {u: self.graph[u].copy() for u in self.vertices}

    def edmonds_karp(self, source, sink):
        """
        Calculates the maximum flow from a source to a sink in the network.

        Args:
            source: The source vertex.
            sink: The sink vertex.

        Returns:
            float: The maximum flow value.
        """
        max_flow = 0
        while True:
            # Find an augmenting path using BFS on the residual graph
            parent, path_flow = self._bfs(source, sink)

            if path_flow == 0:
                break  # No more augmenting paths

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                # Update residual capacities
                self.residual_graph[u][v] -= path_flow
                # Ensure reverse edge exists for residual graph
                if v not in self.residual_graph:
                    self.residual_graph[v] = {}
                if u not in self.residual_graph[v]:
                    self.residual_graph[v][u] = 0
                self.residual_graph[v][u] += path_flow
                v = u

        return max_flow

    def _bfs(self, source, sink):
        """
        A BFS to find an augmenting path in the residual graph.
        """
        parent = {v: None for v in self.vertices}
        queue = deque([(source, float('infinity'))])
        path_flow = {v: 0 for v in self.vertices}
        path_flow[source] = float('infinity')

        while queue:
            u, flow = queue.popleft()
            for v, capacity in self.residual_graph.get(u, {}).items():
                if parent[v] is None and v != source and capacity > 0:
                    parent[v] = u
                    new_flow = min(flow, capacity)
                    if v == sink:
                        return parent, new_flow
                    queue.append((v, new_flow))
        return parent, 0
