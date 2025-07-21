class Tarjan:
    """
    Implementation of Tarjan's algorithm for finding Strongly Connected Components (SCCs)
    in a directed graph.
    """
    def __init__(self, graph):
        """
        Initializes the Tarjan object with a graph.

        Args:
            graph (dict): A dictionary representing the graph's adjacency list.
                          Example: {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: [5], 5: [3]}
        """
        self.graph = graph
        self.vertices = list(graph.keys())
        self.num_vertices = len(self.vertices)
        self.sccs = []
        self.stack = []
        self.on_stack = {v: False for v in self.vertices}
        self.disc = {v: -1 for v in self.vertices}  # Discovery times
        self.low = {v: -1 for v in self.vertices}   # Low-link values
        self.time = 0

    def find_sccs(self):
        """
        Finds all Strongly Connected Components in the graph.

        Returns:
            list: A list of lists, where each inner list is an SCC.
                  Example: [[0, 1, 2], [3, 4, 5]]
        """
        for v in self.vertices:
            if self.disc[v] == -1:
                self._tarjan_dfs(v)
        return self.sccs

    def _tarjan_dfs(self, u):
        """
        A recursive DFS helper for Tarjan's algorithm.
        """
        self.disc[u] = self.time
        self.low[u] = self.time
        self.time += 1
        self.stack.append(u)
        self.on_stack[u] = True

        for v in self.graph.get(u, []):
            if self.disc[v] == -1:
                self._tarjan_dfs(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif self.on_stack[v]:
                self.low[u] = min(self.low[u], self.disc[v])

        # If u is a root node, pop the stack and form an SCC
        if self.low[u] == self.disc[u]:
            scc = []
            while True:
                node = self.stack.pop()
                self.on_stack[node] = False
                scc.append(node)
                if node == u:
                    break
            self.sccs.append(scc)
