class GraphStatistics:
    """
    Computes various statistics for a graph.
    """
    def __init__(self, graph, directed=False):
        """
        Initializes the GraphStatistics object.

        Args:
            graph (dict): An adjacency list representation of the graph.
            directed (bool): Whether the graph is directed.
        """
        self.graph = graph
        self.vertices = list(graph.keys())
        self.directed = directed

    def get_number_of_vertices(self):
        """
        Returns the number of vertices in the graph.
        """
        return len(self.vertices)

    def get_number_of_edges(self):
        """
        Returns the number of edges in the graph.
        """
        num_edges = sum(len(edges) for edges in self.graph.values())
        if not self.directed:
            num_edges //= 2  # Each edge is counted twice in an undirected graph
        return num_edges

    def get_degree_distribution(self):
        """
        Computes the degree distribution of the graph.

        Returns:
            dict: A dictionary where keys are degrees and values are the number of nodes
                  with that degree.
        """
        degree_dist = {}
        for v in self.vertices:
            degree = len(self.graph.get(v, []))
            degree_dist[degree] = degree_dist.get(degree, 0) + 1
        return degree_dist

    def get_average_degree(self):
        """
        Computes the average degree of the graph.
        """
        num_vertices = self.get_number_of_vertices()
        if num_vertices == 0:
            return 0
        total_degree = sum(len(edges) for edges in self.graph.values())
        return total_degree / num_vertices
