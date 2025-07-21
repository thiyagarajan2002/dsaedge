from .graph_traversal import GraphTraversal
from .cycle_detection import CycleDetection
from .graph_statistics import GraphStatistics
from .graph_coloring import GraphColoring
from .articulation_points import ArticulationPoints
from .bridges import Bridges
from .tarjan import Tarjan

class GraphAnalysis:
    """
    A high-level class for performing various analyses on a graph.
    This class combines functionalities from other modules.
    """
    def __init__(self, graph, directed=False):
        """
        Initializes the GraphAnalysis object.

        Args:
            graph (dict): An adjacency list representation of the graph.
            directed (bool): Whether the graph is directed.
        """
        self.graph = graph
        self.directed = directed
        self.vertices = list(graph.keys())

    def get_basic_stats(self):
        """
        Returns basic statistics of the graph.
        """
        stats = GraphStatistics(self.graph, self.directed)
        return {
            "num_vertices": stats.get_number_of_vertices(),
            "num_edges": stats.get_number_of_edges(),
            "average_degree": stats.get_average_degree(),
            "degree_distribution": stats.get_degree_distribution()
        }

    def check_for_cycles(self):
        """
        Checks if the graph contains cycles.
        """
        cycle_detector = CycleDetection(self.graph, self.directed)
        return cycle_detector.has_cycle()

    def find_connected_components(self):
        """
        Finds the connected components of the graph (for undirected graphs).
        If the graph is directed, it finds strongly connected components.
        """
        if self.directed:
            tarjan = Tarjan(self.graph)
            return tarjan.find_sccs()
        else:
            # Using traversal to find connected components
            visited = {v: False for v in self.vertices}
            components = []
            traversal = GraphTraversal(self.graph)
            for v in self.vertices:
                if not visited[v]:
                    component = traversal.bfs(v) # or dfs
                    for node in component:
                        visited[node] = True
                    components.append(component)
            return components

    def find_articulation_points_and_bridges(self):
        """
        Finds articulation points and bridges in an undirected graph.
        """
        if self.directed:
            return "This analysis is for undirected graphs."
        ap_finder = ArticulationPoints(self.graph)
        br_finder = Bridges(self.graph)
        return {
            "articulation_points": ap_finder.find_articulation_points(),
            "bridges": br_finder.find_bridges()
        }

    def get_greedy_coloring(self):
        """
        Performs a greedy coloring of the graph.
        """
        coloring = GraphColoring(self.graph)
        return coloring.greedy_coloring()
