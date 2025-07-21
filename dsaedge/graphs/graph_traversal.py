from collections import deque

class GraphTraversal:
    """
    Provides methods for Breadth-First Search (BFS) and Depth-First Search (DFS)
    on a graph.
    """
    def __init__(self, graph):
        """
        Initializes the GraphTraversal object.

        Args:
            graph (dict): An adjacency list representation of the graph.
                          Example: {'A': ['B', 'C'], 'B': ['D', 'E'], ...}
        """
        self.graph = graph
        self.vertices = list(graph.keys())

    def bfs(self, start_vertex):
        """
        Performs a Breadth-First Search traversal.

        Args:
            start_vertex: The vertex to start the traversal from.

        Returns:
            list: A list of vertices in BFS order.
        """
        if start_vertex not in self.vertices:
            raise ValueError("Start vertex not in graph.")

        visited = {v: False for v in self.vertices}
        queue = deque([start_vertex])
        result = []
        visited[start_vertex] = True

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            for neighbor in self.graph.get(vertex, []):
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return result

    def dfs(self, start_vertex):
        """
        Performs a Depth-First Search traversal.

        Args:
            start_vertex: The vertex to start the traversal from.

        Returns:
            list: A list of vertices in DFS order.
        """
        if start_vertex not in self.vertices:
            raise ValueError("Start vertex not in graph.")

        visited = {v: False for v in self.vertices}
        result = []
        self._dfs_recursive(start_vertex, visited, result)
        return result

    def _dfs_recursive(self, vertex, visited, result):
        """
        A recursive helper for DFS.
        """
        visited[vertex] = True
        result.append(vertex)

        for neighbor in self.graph.get(vertex, []):
            if not visited[neighbor]:
                self._dfs_recursive(neighbor, visited, result)
