
from .tree_properties import height

def is_balanced(root):
    """Checks if the tree is balanced."""
    if root is None:
        return True

    lh = height(root.left)
    rh = height(root.right)

    if abs(lh - rh) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True

    return False

def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    """Checks if the tree is a valid Binary Search Tree."""
    if root is None:
        return True

    if not (min_val < root.data < max_val):
        return False

    return (is_bst(root.left, min_val, root.data) and
            is_bst(root.right, root.data, max_val))

def find_min(root):
    """Finds the minimum value in a binary search tree."""
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.data

def find_max(root):
    """Finds the maximum value in a binary search tree."""
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.data
