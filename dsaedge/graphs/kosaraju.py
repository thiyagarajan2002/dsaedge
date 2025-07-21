class Kosaraju:
    """
    Implementation of Kosaraju's algorithm for finding Strongly Connected Components (SCCs)
    in a directed graph.
    """
    def __init__(self, graph):
        """
        Initializes the Kosaraju object with a graph.

        Args:
            graph (dict): A dictionary representing the graph's adjacency list.
                          Example: {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: [5], 5: [3]}
        """
        self.graph = graph
        self.vertices = list(graph.keys())
        self.num_vertices = len(self.vertices)
        self.sccs = []

    def find_sccs(self):
        """
        Finds all Strongly Connected Components in the graph.

        Returns:
            list: A list of lists, where each inner list is an SCC.
                  Example: [[0, 1, 2], [3, 4, 5]]
        """
        # 1. First DFS to get the finishing times (post-order traversal)
        stack = []
        visited = {v: False for v in self.vertices}
        for v in self.vertices:
            if not visited[v]:
                self._dfs1(v, visited, stack)

        # 2. Get the transpose of the graph
        transposed_graph = self._get_transpose()

        # 3. Second DFS on the transposed graph in the order of finishing times
        visited = {v: False for v in self.vertices}
        while stack:
            v = stack.pop()
            if not visited[v]:
                scc = []
                self._dfs2(v, visited, scc, transposed_graph)
                self.sccs.append(scc)

        return self.sccs

    def _dfs1(self, u, visited, stack):
        """
        First DFS to fill the stack with vertices in order of finishing times.
        """
        visited[u] = True
        for v in self.graph.get(u, []):
            if not visited[v]:
                self._dfs1(v, visited, stack)
        stack.append(u)

    def _dfs2(self, u, visited, scc, transposed_graph):
        """
        Second DFS on the transposed graph to find SCCs.
        """
        visited[u] = True
        scc.append(u)
        for v in transposed_graph.get(u, []):
            if not visited[v]:
                self._dfs2(v, visited, scc, transposed_graph)

    def _get_transpose(self):
        """
        Computes the transpose of the graph.
        """
        transposed_graph = {v: [] for v in self.vertices}
        for u, edges in self.graph.items():
            for v in edges:
                transposed_graph[v].append(u)
        return transposed_graph
