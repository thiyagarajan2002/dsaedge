
class TreeNode:
    """
    A node in a tree data structure.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None  # Optional, useful for some algorithms
        self.color = None   # For Red-Black Trees
        self.height = 1     # For AVL Trees

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"TreeNode({self.data})"
