class GraphColoring:
    """
    Implements a greedy algorithm for vertex coloring of a graph.
    This algorithm does not guarantee the use of the minimum number of colors
    (which is an NP-hard problem), but it provides a valid coloring.
    """
    def __init__(self, graph):
        """
        Initializes the GraphColoring object.

        Args:
            graph (dict): An adjacency list representation of the undirected graph.
                          Example: {0: [1, 2], 1: [0, 2, 3], ...}
        """
        self.graph = graph
        self.vertices = list(graph.keys())
        self.num_vertices = len(self.vertices)

    def greedy_coloring(self):
        """
        Assigns colors to vertices such that no two adjacent vertices share the same color.

        Returns:
            dict: A dictionary mapping each vertex to a color (integer).
                  Example: {0: 0, 1: 1, 2: 2, 3: 0}
        """
        # Initialize all vertices as uncolored
        result = {v: -1 for v in self.vertices}
        # Assign the first color to the first vertex
        result[self.vertices[0]] = 0

        # A temporary array to store the available colors. False value of
        # available[cr] would mean that the color cr is assigned to one of its
        # adjacent vertices.
        available = [False] * self.num_vertices

        # Assign colors to the remaining V-1 vertices
        for u in self.vertices[1:]:
            # Process all adjacent vertices and flag their colors as unavailable
            for v_info in self.graph.get(u, []):
                v = v_info[0] if isinstance(v_info, tuple) else v_info
                if result[v] != -1:
                    available[result[v]] = True

            # Find the first available color
            cr = 0
            while cr < self.num_vertices:
                if not available[cr]:
                    break
                cr += 1

            result[u] = cr  # Assign the found color

            # Reset the values back to false for the next iteration
            for v_info in self.graph.get(u, []):
                v = v_info[0] if isinstance(v_info, tuple) else v_info
                if result[v] != -1:
                    available[result[v]] = False

        return result
