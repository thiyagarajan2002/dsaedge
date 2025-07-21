
from collections import deque

def inorder(root):
    """Performs an in-order traversal of the tree."""
    res = []
    if root:
        res.extend(inorder(root.left))
        res.append(root.data)
        res.extend(inorder(root.right))
    return res

def preorder(root):
    """Performs a pre-order traversal of the tree."""
    res = []
    if root:
        res.append(root.data)
        res.extend(preorder(root.left))
        res.extend(preorder(root.right))
    return res

def postorder(root):
    """Performs a post-order traversal of the tree."""
    res = []
    if root:
        res.extend(postorder(root.left))
        res.extend(postorder(root.right))
        res.append(root.data)
    return res

def level_order(root):
    """Performs a level-order traversal of the tree."""
    if not root:
        return []
    
    res = []
    q = deque([root])
    while q:
        node = q.popleft()
        res.append(node.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res

def reverse_level_order(root):
    """Performs a reverse level-order traversal of the tree."""
    if not root:
        return []
    
    res = []
    q = deque([root])
    while q:
        node = q.popleft()
        res.insert(0, node.data) # Insert at the beginning
        if node.right: # Process right child first
            q.append(node.right)
        if node.left:
            q.append(node.left)
    return res

def zigzag_level_order(root):
    """Performs a zigzag level-order traversal of the tree."""
    if not root:
        return []

    res = []
    q = deque([root])
    left_to_right = True
    while q:
        level_size = len(q)
        current_level = deque()
        for _ in range(level_size):
            node = q.popleft()
            if left_to_right:
                current_level.append(node.data)
            else:
                current_level.appendleft(node.data)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        res.append(list(current_level))
        left_to_right = not left_to_right
        
    # Flatten the list of lists
    return [item for sublist in res for item in sublist]
