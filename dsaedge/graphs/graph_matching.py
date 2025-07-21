from collections import deque

class GraphMatching:
    """
    Implements the Hopcroft-Karp algorithm to find the maximum cardinality matching
    in a bipartite graph.
    """
    def __init__(self, graph):
        """
        Initializes the GraphMatching object.

        Args:
            graph (dict): An adjacency list representation of the bipartite graph.
                          The graph should be specified for one set of vertices (U),
                          with edges pointing to the other set (V).
                          Example: {'u1': ['v1', 'v2'], 'u2': ['v1'], ...}
        """
        self.graph = graph
        self.u_vertices = list(graph.keys())
        # Infer v_vertices from the edges
        v_set = set()
        for edges in graph.values():
            v_set.update(edges)
        self.v_vertices = list(v_set)

        self.pair_u = {}
        self.pair_v = {}
        self.dist = {}
        self.NIL = 0 # Represents a null vertex

    def hopcroft_karp(self):
        """
        Finds the maximum cardinality matching in the bipartite graph.

        Returns:
            int: The size of the maximum matching.
        """
        # Initialize pairs for all vertices in U and V
        for u in self.u_vertices:
            self.pair_u[u] = self.NIL
        for v in self.v_vertices:
            self.pair_v[v] = self.NIL

        matching = 0
        while self._bfs():
            for u in self.u_vertices:
                if self.pair_u[u] == self.NIL:
                    if self._dfs(u):
                        matching += 1
        return matching

    def _bfs(self):
        """
        BFS to build layers of augmenting paths.
        """
        queue = deque()
        for u in self.u_vertices:
            if self.pair_u[u] == self.NIL:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')

        self.dist[self.NIL] = float('inf')

        while queue:
            u = queue.popleft()
            if self.dist[u] < self.dist[self.NIL]:
                for v in self.graph.get(u, []):
                    if self.dist.get(self.pair_v[v], float('inf')) == float('inf'):
                        self.dist[self.pair_v[v]] = self.dist[u] + 1
                        queue.append(self.pair_v[v])
        return self.dist[self.NIL] != float('inf')

    def _dfs(self, u):
        """
        DFS to find an augmenting path.
        """
        if u != self.NIL:
            for v in self.graph.get(u, []):
                if self.dist.get(self.pair_v[v], float('inf')) == self.dist[u] + 1:
                    if self._dfs(self.pair_v[v]):
                        self.pair_v[v] = u
                        self.pair_u[u] = v
                        return True
            self.dist[u] = float('inf')
            return False
        return True
