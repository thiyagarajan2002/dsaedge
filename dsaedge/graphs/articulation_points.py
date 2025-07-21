class ArticulationPoints:
    """
    Finds articulation points (or cut vertices) in an undirected graph.
    An articulation point is a vertex whose removal increases the number of
    connected components in the graph.
    """
    def __init__(self, graph):
        """
        Initializes the ArticulationPoints object.

        Args:
            graph (dict): An adjacency list representation of the undirected graph.
                          Example: {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3]}
        """
        self.graph = graph
        self.vertices = list(graph.keys())
        self.num_vertices = len(self.vertices)
        self.time = 0
        self.disc = {v: -1 for v in self.vertices}  # Discovery times
        self.low = {v: -1 for v in self.vertices}   # Low-link values
        self.parent = {v: -1 for v in self.vertices}
        self.articulation_points = set()

    def find_articulation_points(self):
        """
        Finds all articulation points in the graph.

        Returns:
            set: A set of articulation points.
                 Example: {2, 3}
        """
        for v in self.vertices:
            if self.disc[v] == -1:
                self._find_ap_util(v)
        return self.articulation_points

    def _find_ap_util(self, u):
        """
        A recursive DFS utility to find articulation points.
        """
        self.disc[u] = self.time
        self.low[u] = self.time
        self.time += 1
        children = 0

        for v in self.graph.get(u, []):
            if v == self.parent[u]:
                continue

            if self.disc[v] != -1:  # Back edge
                self.low[u] = min(self.low[u], self.disc[v])
            else:  # Tree edge
                children += 1
                self.parent[v] = u
                self._find_ap_util(v)
                self.low[u] = min(self.low[u], self.low[v])

                # Case 1: u is the root of DFS tree and has two or more children.
                if self.parent[u] == -1 and children > 1:
                    self.articulation_points.add(u)

                # Case 2: u is not root and low value of one of its children is more
                # than discovery value of u.
                if self.parent[u] != -1 and self.low[v] >= self.disc[u]:
                    self.articulation_points.add(u)
