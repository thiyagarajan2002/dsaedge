# dsaedge: Data Structures and Algorithms in Python

A comprehensive collection of various data structures and algorithms implemented in Python.

## Installation

You can install this package using pip:

```bash
pip install dsaedge
```

## Usage

Here are some examples of how to use the implemented data structures and algorithms:

### Advanced Data Structures

```python
# Disjoint Set Union (DSU)
from dsaedge.advanced_data_structures.disjoint_set_union import DSU

dsu = DSU()
dsu.make_set(1)
dsu.make_set(2)
dsu.make_set(3)
dsu.union(1, 2)
print(f"DSU - Find(1): {dsu.find(1)}")
print(f"DSU - Find(2): {dsu.find(2)}")
print(f"DSU - Are 1 and 3 in the same set? {dsu.find(1) == dsu.find(3)}")

# Fenwick Tree (Binary Indexed Tree)
from dsaedge.advanced_data_structures.fenwick_tree import FenwickTree

ft = FenwickTree(10)
ft.update(0, 5)  # Add 5 to index 0
ft.update(4, 3)  # Add 3 to index 4
print(f"Fenwick Tree - Sum up to index 0: {ft.query(0)}")
print(f"Fenwick Tree - Sum up to index 4: {ft.query(4)}")
print(f"Fenwick Tree - Sum in range [0, 4]: {ft.range_query(0, 4)}")

# Segment Tree
from dsaedge.advanced_data_structures.segment_tree import SegmentTree

arr_seg = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr_seg)
print(f"Segment Tree - Sum of range [1, 4]: {st.query(1, 4)}")
st.update(2, 10)  # Update index 2 to 10
print(f"Segment Tree - Sum of range [1, 4] after update: {st.query(1, 4)}")

# Trie (Prefix Tree)
from dsaedge.advanced_data_structures.trie import Trie

trie = Trie()
trie.insert("apple")
trie.insert("apricot")
print(f"Trie - Search 'apple': {trie.search('apple')}")
print(f"Trie - Search 'app': {trie.search('app')}")
print(f"Trie - Starts with 'app': {trie.starts_with('app')}")
print(f"Trie - Starts with 'ban': {trie.starts_with('ban')}")
```

### Algorithmic Paradigms

```python
# Knuth-Morris-Pratt (KMP) string searching
from dsaedge.algorithmic_paradigms.kmp_search import kmp_search

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
occurrences = kmp_search(text, pattern)
print(f"KMP Search - Pattern found at indices: {occurrences}")

# 0/1 Knapsack Problem
from dsaedge.algorithmic_paradigms.knapsack_problem import knapsack_01

weights = [1, 2, 3, 8, 7]
values = [20, 5, 10, 40, 15]
capacity = 10
max_value = knapsack_01(weights, values, capacity)
print(f"Knapsack Problem - Maximum value: {max_value}")

# Longest Common Subsequence (LCS)
from dsaedge.algorithmic_paradigms.longest_common_subsequence import longest_common_subsequence, reconstruct_lcs

s1 = "AGGTAB"
s2 = "GXTXAYB"
lcs_length = longest_common_subsequence(s1, s2)
lcs_string = reconstruct_lcs(s1, s2)
print(f"LCS - Length: {lcs_length}, Subsequence: {lcs_string}")

# N-Queens Problem
from dsaedge.algorithmic_paradigms.n_queens import solve_n_queens

n_queens_solutions = solve_n_queens(4)
print(f"N-Queens Problem - Solutions for N=4: {len(n_queens_solutions)}")
for sol in n_queens_solutions:
    for row in sol:
        print(row)
    print()

# Sudoku Solver
from dsaedge.algorithmic_paradigms.sudoku_solver import solve_sudoku, print_board

sudoku_board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
print("Sudoku Solver - Original Board:")
print_board(sudoku_board)
if solve_sudoku(sudoku_board):
    print("
Sudoku Solver - Solved Board:")
    print_board(sudoku_board)
else:
    print("
Sudoku Solver - No solution exists.")
```

### Graphs

```python
# Graph Representation (Adjacency List) and Algorithms (BFS, DFS, Dijkstra, Prim)
from dsaedge.graphs.graph_representation import Graph

g = Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)

print(f"Graph - BFS from A: {g.bfs('A')}")
print(f"Graph - DFS from A: {g.dfs('A')}")

distances_dijkstra, _ = g.dijkstra('A')
print(f"Graph - Dijkstra distances from A: {distances_dijkstra}")

mst_cost, mst_edges = g.prims_algorithm('A')
print(f"Graph - Prim's MST cost: {mst_cost}, Edges: {mst_edges}")

# Kruskal's Algorithm
from dsaedge.graphs.kruskal_algorithm import kruskal_algorithm

vertices_kruskal = ['A', 'B', 'C', 'D', 'E']
edges_kruskal = [
    (1, 'A', 'B'), (4, 'A', 'C'), (2, 'B', 'C'),
    (5, 'B', 'D'), (1, 'C', 'D'), (3, 'D', 'E')
]
mst_cost_kruskal, mst_edges_kruskal = kruskal_algorithm(vertices_kruskal, edges_kruskal)
print(f"Kruskal's Algorithm - MST cost: {mst_cost_kruskal}, Edges: {mst_edges_kruskal}")

# Topological Sort
from dsaedge.graphs.topological_sort import Graph as TopologicalGraph, topological_sort

g_ts = TopologicalGraph(6)
g_ts.add_edge(5, 2)
g_ts.add_edge(5, 0)
g_ts.add_edge(4, 0)
g_ts.add_edge(4, 1)
g_ts.add_edge(2, 3)
g_ts.add_edge(3, 1)

top_order = topological_sort(g_ts)
print(f"Topological Sort - Order: {top_order}")
```

### Hash Tables

```python
# Hash Table
from dsaedge.hash_tables.hash_table import HashTable

ht = HashTable()
ht.set("name", "Alice")
ht.set("age", 30)
ht["city"] = "New York" # Using dictionary-style assignment

print(f"Hash Table - Name: {ht.get('name')}")
print(f"Hash Table - City: {ht['city']}")

try:
    print(f"Hash Table - Occupation: {ht.get('occupation')}")
except KeyError as e:
    print(f"Hash Table - Error: {e}")

del ht["age"] # Using dictionary-style deletion
print(f"Hash Table - After deleting age: {ht}")
```

### Heaps

```python
# Min-Heap
from dsaedge.heaps.min_heap import MinHeap

min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(4)
min_heap.insert(1)
min_heap.insert(5)

print(f"Min-Heap - Min element: {min_heap.get_min()}")
print(f"Min-Heap - Extracted min: {min_heap.extract_min()}")
print(f"Min-Heap - New min element: {min_heap.get_min()}")
print(f"Min-Heap - Is empty: {min_heap.is_empty()}")
print(f"Min-Heap - Size: {min_heap.size()}")
```

### Linked Lists

```python
# Singly Linked List
from dsaedge.linked_lists.singly_linked_list import SinglyLinkedList

sll = SinglyLinkedList()
sll.append(10)
sll.prepend(5)
sll.insert_at_position(7, 1)
print(f"Singly Linked List: {sll}")
sll.delete(7)
print(f"Singly Linked List after deleting 7: {sll}")
print(f"Singly Linked List - Length: {len(sll)}")

# Doubly Linked List
from dsaedge.linked_lists.doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList()
dll.append(1)
dll.prepend(0)
dll.insert_at_position(2, 2)
print(f"Doubly Linked List: {dll}")
dll.delete(1)
print(f"Doubly Linked List after deleting 1: {dll}")

# Circular Singly Linked List
from dsaedge.linked_lists.circular_singly_linked_list import CircularSinglyLinkedList

csll = CircularSinglyLinkedList()
csll.append(1)
csll.append(2)
csll.prepend(0)
print(f"Circular Singly Linked List: {csll}")
csll.delete(1)
print(f"Circular Singly Linked List after deleting 1: {csll}")

# Circular Doubly Linked List
from dsaedge.linked_lists.circular_doubly_linked_list import CircularDoublyLinkedList

cdll = CircularDoublyLinkedList()
cdll.append(10)
cdll.append(20)
cdll.prepend(5)
print(f"Circular Doubly Linked List: {cdll.display()}")
```

### Queue

```python
# Queue (implemented with Linked List)
from dsaedge.queue import Queue

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(f"Queue: {q.display()}")
print(f"Peek: {q.peek()}")
q.dequeue()
print(f"Queue after dequeue: {q.display()}")
```

### Stack

```python
# Stack (implemented with Linked List)
from dsaedge.stack import Stack

s = Stack()
s.push(100)
s.push(200)
print(f"Stack: {s.display()}")
print(f"Peek: {s.peek()}")
s.pop()
print(f"Stack after pop: {s.display()}")
```

### Searching

```python
# Searching Algorithms
from dsaedge.searching.linear_search import Linear_Search
from dsaedge.searching.binary_search import Binary_Search, Binary_Search_Recursive

arr_search = [1, 5, 2, 8, 3, 9, 4]
target_linear = 8
print(f"Linear Search - Index of {target_linear}: {Linear_Search(arr_search, target_linear)}")

arr_sorted = [1, 2, 3, 4, 5, 8, 9]
target_binary = 4
print(f"Binary Search (Iterative) - Index of {target_binary}: {Binary_Search(arr_sorted, target_binary)}")
print(f"Binary Search (Recursive) - Index of {target_binary}: {Binary_Search_Recursive(arr_sorted, 0, len(arr_sorted) - 1, target_binary)}")
```

### Sorting

```python
# Sorting Algorithms
from dsaedge.sorting.bubble_sort import Bubble_Sort
from dsaedge.sorting.heap_sort import Heap_Sort
from dsaedge.sorting.insertion_sort import Insertion_Sort
from dsaedge.sorting.merge_sort import Merge_Sort
from dsaedge.sorting.quick_sort import Quick_Sort
from dsaedge.sorting.selection_sort import Selection_Sort

arr_sort = [64, 34, 25, 12, 22, 11, 90]

# These functions sort the list in-place and return it.
print(f"Original Array: {arr_sort}")
print(f"Bubble Sort: {Bubble_Sort(arr_sort[:])}")
print(f"Heap Sort: {Heap_Sort(arr_sort[:])}")
print(f"Insertion Sort: {Insertion_Sort(arr_sort[:])}")
print(f"Merge Sort: {Merge_Sort(arr_sort[:])}")
print(f"Quick Sort: {Quick_Sort(arr_sort[:])}")
print(f"Selection Sort: {Selection_Sort(arr_sort[:])}")
```

### Trees

```python
# Binary Search Tree (BST)
from dsaedge.trees.binary_search_tree import BinarySearchTree

bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
print(f"BST - Search 40: {bst.search(40).data if bst.search(40) else None}")
bst.delete(30)
print(f"BST - In-order traversal after deleting 30: {bst.in_order_traversal()}")

# AVL Tree
from dsaedge.trees.avl_tree import AVLTree

avl = AVLTree()
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)
avl.insert(50)
avl.insert(25)
print(f"AVL Tree - In-order traversal: {avl.in_order_traversal()}")
avl.delete(30)
print(f"AVL Tree - In-order traversal after deleting 30: {avl.in_order_traversal()}")
```

## Implemented Data Structures and Algorithms

The `dsaedge` package is organized into several modules, each focusing on a specific category of data structures or algorithms.

### Data Structures

*   **`advanced_data_structures`**
    *   `disjoint_set_union.py`: Disjoint Set Union (DSU) with path compression and union by size.
    *   `fenwick_tree.py`: Fenwick Tree (Binary Indexed Tree) for prefix sums.
    *   `segment_tree.py`: Segment Tree for range queries and point updates.
    *   `trie.py`: Trie (Prefix Tree) for string searching.
*   **`hash_tables`**
    *   `hash_table.py`: Hash Table with chaining for collision resolution.
*   **`heaps`**
    *   `min_heap.py`: Min-Heap implementation.
*   **`linked_lists`**
    *   `singly_linked_list.py`: Standard Singly Linked List.
    *   `doubly_linked_list.py`: Standard Doubly Linked List.
    *   `circular_singly_linked_list.py`: Circular Singly Linked List.
    *   `circular_doubly_linked_list.py`: Circular Doubly Linked List.
*   **`queue`**
    *   `queue.py`: Queue implementation using a linked list.
*   **`stack`**
    *   `stack.py`: Stack implementation using a linked list.
*   **`trees`**
    *   `binary_tree.py`: Generic Binary Tree with traversal methods.
    *   `binary_search_tree.py`: Binary Search Tree (BST).
    *   `avl_tree.py`: Self-balancing AVL Tree.
    *   `red_black_tree.py`: Self-balancing Red-Black Tree.
    *   `splay_tree.py`: Self-balancing Splay Tree.
    *   `tree_node.py`: Generic tree node class.
    *   And modules for tree-related operations, properties, traversals, utilities, exceptions, serialization, and visualization.

### Algorithms

*   **`algorithmic_paradigms`**
    *   `kmp_search.py`: Knuth-Morris-Pratt (KMP) string searching.
    *   `knapsack_problem.py`: 0/1 Knapsack problem (Dynamic Programming).
    *   `longest_common_subsequence.py`: Longest Common Subsequence (LCS) (Dynamic Programming).
    *   `n_queens.py`: N-Queens problem solver (Backtracking).
    *   `sudoku_solver.py`: Sudoku solver (Backtracking).
*   **`graphs`**
    *   `graph_representation.py`: Basic graph representation with BFS, DFS, Dijkstra's, and Prim's.
    *   `bellman_ford.py`: Bellman-Ford algorithm for shortest paths with negative weights.
    *   `dijkstra.py`: Dijkstra's algorithm for single-source shortest paths.
    *   `floyd_warshall.py`: Floyd-Warshall algorithm for all-pairs shortest paths.
    *   `johnson.py`: Johnson's algorithm for all-pairs shortest paths in sparse graphs.
    *   `kruskal_algorithm.py`: Kruskal's algorithm for Minimum Spanning Tree (MST).
    *   `prim.py`: Prim's algorithm for Minimum Spanning Tree (MST).
    *   `topological_sort.py`: Topological Sort for Directed Acyclic Graphs (DAG).
    *   `cycle_detection.py`: Detects cycles in directed and undirected graphs.
    *   `articulation_points.py`: Finds articulation points (cut vertices).
    *   `bridges.py`: Finds bridges in a graph.
    *   `biconnected_components.py`: Finds biconnected components.
    *   `kosaraju.py`: Kosaraju's algorithm for Strongly Connected Components (SCCs).
    *   `tarjan.py`: Tarjan's algorithm for Strongly Connected Components (SCCs).
    *   `network_flow.py`: Edmonds-Karp algorithm for maximum flow.
    *   `graph_matching.py`: Hopcroft-Karp algorithm for maximum bipartite matching.
    *   `graph_coloring.py`: Greedy algorithm for vertex coloring.
    *   `graph_partitioning.py`: Kernighan-Lin algorithm for graph partitioning.
    *   `graph_clustering.py`: Girvan-Newman algorithm for community detection.
    *   And modules for graph analysis, search, statistics, utilities, and more.
*   **`searching`**
    *   `linear_search.py`: Linear Search.
    *   `binary_search.py`: Binary Search (iterative and recursive).
*   **`sorting`**
    *   `bubble_sort.py`: Bubble Sort.
    *   `selection_sort.py`: Selection Sort.
    *   `insertion_sort.py`: Insertion Sort.
    *   `merge_sort.py`: Merge Sort.
    *   `quick_sort.py`: Quick Sort.
    *   `heap_sort.py`: Heap Sort.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
