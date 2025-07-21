class BiconnectedComponents:
    """
    Finds biconnected components (BCCs) in an undirected graph.
    A BCC is a maximal subgraph where any two vertices are connected by at least two
    vertex-disjoint paths.
    This implementation uses an algorithm based on DFS and tracking discovery times
    and low-link values, similar to finding articulation points and bridges.
    """
    def __init__(self, graph):
        """
        Initializes the BiconnectedComponents object.

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
        self.edge_stack = []
        self.bccs = []

    def find_bccs(self):
        """
        Finds all biconnected components in the graph.

        Returns:
            list: A list of lists, where each inner list contains the edges of a BCC.
                  Example: [[(0, 1), (1, 2), (2, 0)], [(2, 3), (3, 4)]]
        """
        for v in self.vertices:
            if self.disc[v] == -1:
                self._find_bccs_util(v)

            # If there are remaining edges in the stack, they form a BCC
            # This handles the case where the entire graph is one BCC
            if self.edge_stack:
                component = []
                while self.edge_stack:
                    component.append(self.edge_stack.pop())
                self.bccs.append(component)

        return self.bccs

    def _find_bccs_util(self, u):
        """
        A recursive DFS utility to find BCCs.
        """
        self.disc[u] = self.time
        self.low[u] = self.time
        self.time += 1

        for v in self.graph.get(u, []):
            if v == self.parent[u]:
                continue

            if self.disc[v] != -1:  # Back edge
                self.low[u] = min(self.low[u], self.disc[v])
                if self.disc[v] < self.disc[u]: # Important condition to only add edge once
                    self.edge_stack.append((u, v))
            else:  # Tree edge
                self.parent[v] = u
                self.edge_stack.append((u, v))
                self._find_bccs_util(v)
                self.low[u] = min(self.low[u], self.low[v])

                # If u is an articulation point, pop edges from stack to form a BCC
                if self.low[v] >= self.disc[u]:
                    component = []
                    while True:
                        edge = self.edge_stack.pop()
                        component.append(edge)
                        if edge == (u, v):
                            break
                    self.bccs.append(component)
