class GraphUtils:
    """
    Provides utility functions for graph manipulation and analysis.
    """
    def __init__(self, graph):
        """
        Initializes the GraphUtils object.

        Args:
            graph (dict): An adjacency list representation of the graph.
        """
        self.graph = graph
        self.vertices = list(graph.keys())

    def get_transpose(self):
        """
        Computes the transpose of a directed graph.

        Returns:
            dict: The adjacency list of the transposed graph.
        """
        transposed_graph = {v: [] for v in self.vertices}
        for u, edges in self.graph.items():
            for v in edges:
                # This handles both weighted and unweighted graphs
                if isinstance(v, tuple):
                    neighbor, weight = v
                    transposed_graph[neighbor].append((u, weight))
                else:
                    transposed_graph[v].append(u)
        return transposed_graph

    def is_bipartite(self):
        """
        Checks if the graph is bipartite using BFS and coloring.
        Assumes the graph is undirected.

        Returns:
            bool: True if the graph is bipartite, False otherwise.
        """
        color = {}
        for v_start in self.vertices:
            if v_start not in color:
                color[v_start] = 1  # 1 for one color, -1 for the other
                queue = [v_start]
                while queue:
                    u = queue.pop(0)
                    for v_info in self.graph.get(u, []):
                        v = v_info[0] if isinstance(v_info, tuple) else v_info
                        if v not in color:
                            color[v] = -color[u]
                            queue.append(v)
                        elif color[v] == color[u]:
                            return False
        return True

    def get_degree(self, vertex):
        """
        Calculates the degree of a vertex in an undirected graph.
        For a directed graph, this returns the out-degree.
        """
        return len(self.graph.get(vertex, []))
