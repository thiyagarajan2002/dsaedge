from collections import deque

class GraphClustering:
    """
    Implements the Girvan-Newman algorithm for community detection in graphs.
    This algorithm identifies communities by progressively removing edges with the
    highest betweenness centrality.
    """
    def __init__(self, graph):
        """
        Initializes the GraphClustering object.

        Args:
            graph (dict): An adjacency list representation of the undirected graph.
                          Example: {'A': ['B', 'C'], 'B': ['A', 'D'], ...}
        """
        self.graph = graph
        self.vertices = list(graph.keys())
        self.num_vertices = len(self.vertices)
        self.original_graph = {u: list(v) for u, v in graph.items()} # Deep copy for restoration

    def girvan_newman(self):
        """
        Performs the Girvan-Newman algorithm.
        This is a simplified version that returns the components after one iteration
        of removing the highest betweenness edge(s).

        Returns:
            list: A list of lists, where each inner list is a community (a connected component).
        """
        # 1. Calculate betweenness for all edges
        edge_betweenness = self._calculate_edge_betweenness()

        if not edge_betweenness:
            return [self.vertices] # Graph is a single node or disconnected nodes

        # 2. Find the edge(s) with the highest betweenness
        max_betweenness = max(edge_betweenness.values())
        edges_to_remove = [edge for edge, betweenness in edge_betweenness.items() if betweenness == max_betweenness]

        # 3. Remove the edge(s)
        for u, v in edges_to_remove:
            if v in self.graph[u]: self.graph[u].remove(v)
            if u in self.graph[v]: self.graph[v].remove(u)

        # 4. Find the connected components (communities)
        communities = self._get_connected_components()

        # Restore graph for potential future calls
        self.graph = {u: list(v) for u, v in self.original_graph.items()}

        return communities

    def _calculate_edge_betweenness(self):
        edge_betweenness = {tuple(sorted((u, v))): 0.0 for u in self.graph for v in self.graph[u]}

        for s in self.vertices:
            # BFS from s
            stack = []
            parent = {v: [] for v in self.vertices}
            sigma = {v: 0 for v in self.vertices}; sigma[s] = 1
            dist = {v: -1 for v in self.vertices}; dist[s] = 0
            queue = deque([s])

            while queue:
                v = queue.popleft()
                stack.append(v)
                for w in self.graph.get(v, []):
                    if dist[w] < 0:
                        queue.append(w)
                        dist[w] = dist[v] + 1
                    if dist[w] == dist[v] + 1:
                        sigma[w] += sigma[v]
                        parent[w].append(v)

            # Accumulate betweenness
            delta = {v: 0 for v in self.vertices}
            while stack:
                w = stack.pop()
                for v in parent[w]:
                    credit = (sigma[v] / sigma[w]) * (1 + delta[w])
                    edge = tuple(sorted((v, w)))
                    edge_betweenness[edge] += credit
                    delta[v] += credit
        return edge_betweenness

    def _get_connected_components(self):
        visited = {v: False for v in self.vertices}
        components = []
        for v in self.vertices:
            if not visited[v]:
                component = []
                self._dfs_components(v, visited, component)
                components.append(component)
        return components

    def _dfs_components(self, u, visited, component):
        visited[u] = True
        component.append(u)
        for v in self.graph.get(u, []):
            if not visited[v]:
                self._dfs_components(v, visited, component)
