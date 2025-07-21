from collections import deque

class GraphSearch:
    """
    Provides methods to find a path between two vertices in a graph using
    Breadth-First Search (BFS) and Depth-First Search (DFS).
    """
    def __init__(self, graph):
        """
        Initializes the GraphSearch object.

        Args:
            graph (dict): An adjacency list representation of the graph.
                          Example: {'A': ['B', 'C'], 'B': ['D', 'E'], ...}
        """
        self.graph = graph
        self.vertices = list(graph.keys())

    def find_path_bfs(self, start_vertex, end_vertex):
        """
        Finds a path from start_vertex to end_vertex using BFS.

        Args:
            start_vertex: The starting vertex.
            end_vertex: The ending vertex.

        Returns:
            list: A list of vertices representing the path, or None if no path exists.
        """
        if start_vertex not in self.vertices or end_vertex not in self.vertices:
            return None

        queue = deque([(start_vertex, [start_vertex])])
        visited = {start_vertex}

        while queue:
            current_vertex, path = queue.popleft()

            if current_vertex == end_vertex:
                return path

            for neighbor in self.graph.get(current_vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path))
        return None

    def find_path_dfs(self, start_vertex, end_vertex):
        """
        Finds a path from start_vertex to end_vertex using DFS.

        Args:
            start_vertex: The starting vertex.
            end_vertex: The ending vertex.

        Returns:
            list: A list of vertices representing the path, or None if no path exists.
        """
        if start_vertex not in self.vertices or end_vertex not in self.vertices:
            return None

        stack = [(start_vertex, [start_vertex])]
        visited = {start_vertex}

        while stack:
            current_vertex, path = stack.pop()

            if current_vertex == end_vertex:
                return path

            for neighbor in self.graph.get(current_vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append((neighbor, new_path))
        return None
