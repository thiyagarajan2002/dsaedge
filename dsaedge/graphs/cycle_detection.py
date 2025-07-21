class CycleDetection:
    """
    Provides methods to detect cycles in both directed and undirected graphs.
    """
    def __init__(self, graph, directed=True):
        """
        Initializes the CycleDetection object.

        Args:
            graph (dict): An adjacency list representation of the graph.
                          Example: {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
            directed (bool): True if the graph is directed, False otherwise.
        """
        self.graph = graph
        self.vertices = list(graph.keys())
        self.directed = directed

    def has_cycle(self):
        """
        Checks if the graph contains a cycle.

        Returns:
            bool: True if a cycle is found, False otherwise.
        """
        if self.directed:
            return self._has_cycle_directed()
        else:
            return self._has_cycle_undirected()

    def _has_cycle_directed(self):
        """
        Detects a cycle in a directed graph using DFS.
        """
        visited = {v: False for v in self.vertices}
        recursion_stack = {v: False for v in self.vertices}

        for v in self.vertices:
            if not visited[v]:
                if self._dfs_directed_util(v, visited, recursion_stack):
                    return True
        return False

    def _dfs_directed_util(self, u, visited, recursion_stack):
        """
        A recursive DFS utility for directed cycle detection.
        """
        visited[u] = True
        recursion_stack[u] = True

        for v in self.graph.get(u, []):
            if not visited[v]:
                if self._dfs_directed_util(v, visited, recursion_stack):
                    return True
            elif recursion_stack[v]:
                return True

        recursion_stack[u] = False
        return False

    def _has_cycle_undirected(self):
        """
        Detects a cycle in an undirected graph using DFS.
        """
        visited = {v: False for v in self.vertices}

        for v in self.vertices:
            if not visited[v]:
                if self._dfs_undirected_util(v, visited, -1): # -1 as parent for starting node
                    return True
        return False

    def _dfs_undirected_util(self, u, visited, parent):
        """
        A recursive DFS utility for undirected cycle detection.
        """
        visited[u] = True

        for v in self.graph.get(u, []):
            if not visited[v]:
                if self._dfs_undirected_util(v, visited, u):
                    return True
            elif v != parent:
                return True

        return False
