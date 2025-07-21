
from .tree_node import TreeNode

def insert(root, data):
    """Inserts a new node with the given data into the binary search tree."""
    if root is None:
        return TreeNode(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

def delete(root, data):
    """Deletes a node with the given data from the binary search tree."""
    if root is None:
        return root

    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = _find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
        
    return root

def _find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def search(root, data):
    """Searches for a node with the given data in the binary search tree."""
    if root is None or root.data == data:
        return root
    if data < root.data:
        return search(root.left, data)
    return search(root.right, data)

def traverse(root, order='inorder'):
    """Traverses the tree in the specified order."""
    if order == 'inorder':
        return inorder(root)
    elif order == 'preorder':
        return preorder(root)
    elif order == 'postorder':
        return postorder(root)
    else:
        raise ValueError("Invalid traversal order. Choose from 'inorder', 'preorder', or 'postorder'.")

def rotate_left(node):
    """Performs a left rotation on the given node."""
    if not node or not node.right:
        return node
    new_root = node.right
    node.right = new_root.left
    if new_root.left:
        new_root.left.parent = node
    new_root.parent = node.parent
    if not node.parent:
        # If node was the root, new_root is now the root
        pass
    elif node == node.parent.left:
        node.parent.left = new_root
    else:
        node.parent.right = new_root
    new_root.left = node
    node.parent = new_root
    return new_root

def rotate_right(node):
    """Performs a right rotation on the given node."""
    if not node or not node.left:
        return node
    new_root = node.left
    node.left = new_root.right
    if new_root.right:
        new_root.right.parent = node
    new_root.parent = node.parent
    if not node.parent:
        pass
    elif node == node.parent.right:
        node.parent.right = new_root
    else:
        node.parent.left = new_root
    new_root.right = node
    node.parent = new_root
    return new_root

def rebalance(node):
    """Rebalances the tree starting from the given node."""
    # This is a placeholder. The actual implementation depends on the type of self-balancing tree.
    pass

# Helper functions for traverse
def inorder(root):
    res = []
    if root:
        res.extend(inorder(root.left))
        res.append(root.data)
        res.extend(inorder(root.right))
    return res

def preorder(root):
    res = []
    if root:
        res.append(root.data)
        res.extend(preorder(root.left))
        res.extend(preorder(root.right))
    return res

def postorder(root):
    res = []
    if root:
        res.extend(postorder(root.left))
        res.extend(postorder(root.right))
        res.append(root.data)
    return res
