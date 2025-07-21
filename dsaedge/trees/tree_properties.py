
from .tree_node import TreeNode

def is_empty(root):
    """Checks if the tree is empty."""
    return root is None

def size(root):
    """Returns the number of nodes in the tree."""
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)

def height(root):
    """Returns the height of the tree."""
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))

def depth(root, node_data):
    """Returns the depth of a node with the given data."""
    return _depth_helper(root, node_data, 0)

def _depth_helper(current, data, current_depth):
    if current is None:
        return -1
    if current.data == data:
        return current_depth
    
    left_depth = _depth_helper(current.left, data, current_depth + 1)
    if left_depth != -1:
        return left_depth
    
    return _depth_helper(current.right, data, current_depth + 1)

def balance_factor(node):
    """Calculates the balance factor of a node."""
    if node is None:
        return 0
    return height(node.left) - height(node.right)

def is_full(root):
    """Checks if the tree is a full binary tree."""
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return is_full(root.left) and is_full(root.right)
    return False

def is_complete(root):
    """Checks if the tree is a complete binary tree."""
    if root is None:
        return True
    
    q = [root]
    found_non_full = False
    while q:
        node = q.pop(0)
        if node:
            if found_non_full:
                return False
            q.append(node.left)
            q.append(node.right)
        else:
            found_non_full = True
    return True

def is_perfect(root):
    """Checks if the tree is a perfect binary tree."""
    h = height(root)
    return size(root) == (2**(h + 1) - 1)

def is_subtree(main_tree_root, subtree_root):
    """Checks if one tree is a subtree of another."""
    if subtree_root is None:
        return True
    if main_tree_root is None:
        return False
    
    if _are_identical(main_tree_root, subtree_root):
        return True
    
    return is_subtree(main_tree_root.left, subtree_root) or is_subtree(main_tree_root.right, subtree_root)

def _are_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    
    return (root1.data == root2.data and 
            _are_identical(root1.left, root2.left) and 
            _are_identical(root1.right, root2.right))

def is_isomorphic(root1, root2):
    """Checks if two trees are isomorphic."""
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False
        
    return ((is_isomorphic(root1.left, root2.left) and is_isomorphic(root1.right, root2.right)) or
            (is_isomorphic(root1.left, root2.right) and is_isomorphic(root1.right, root2.left)))
