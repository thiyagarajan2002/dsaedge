class Bridges:
    """
    Finds bridges in an undirected graph.
    A bridge is an edge whose removal increases the number of connected components.
    """
    def __init__(self, graph):
        """
        Initializes the Bridges object.

        Args:
            graph (dict): An adjacency list representation of the undirected graph.
                          Example: {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3, 5], 5: [4]}
        """
        self.graph = graph
        self.vertices = list(graph.keys())
        self.num_vertices = len(self.vertices)
        self.time = 0
        self.disc = {v: -1 for v in self.vertices}  # Discovery times
        self.low = {v: -1 for v in self.vertices}   # Low-link values
        self.parent = {v: -1 for v in self.vertices}
        self.bridges = []

    def find_bridges(self):
        """
        Finds all bridges in the graph.

        Returns:
            list: A list of tuples, where each tuple is a bridge.
                  Example: [(2, 3), (3, 4), (4, 5)]
        """
        for v in self.vertices:
            if self.disc[v] == -1:
                self._find_bridges_util(v)
        return self.bridges

    def _find_bridges_util(self, u):
        """
        A recursive DFS utility to find bridges.
        """
        self.disc[u] = self.time
        self.low[u] = self.time
        self.time += 1

        for v in self.graph.get(u, []):
            if v == self.parent[u]:
                continue

            if self.disc[v] != -1:  # Back edge
                self.low[u] = min(self.low[u], self.disc[v])
            else:  # Tree edge
                self.parent[v] = u
                self._find_bridges_util(v)
                self.low[u] = min(self.low[u], self.low[v])

                # If the lowest vertex reachable from subtree under v is below u in DFS tree,
                # then u-v is a bridge.
                if self.low[v] > self.disc[u]:
                    self.bridges.append((u, v))
