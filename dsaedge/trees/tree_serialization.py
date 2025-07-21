
import json
from .tree_node import TreeNode

def serialize_tree(root):
    """Serializes a binary tree to a JSON string."""
    if not root:
        return None

    def to_dict(node):
        if not node:
            return None
        return {
            'data': node.data,
            'left': to_dict(node.left),
            'right': to_dict(node.right)
        }

    return json.dumps(to_dict(root), indent=4)

def deserialize_tree(json_string):
    """Deserializes a JSON string to a binary tree."""
    if not json_string:
        return None

    def to_tree(data):
        if not data:
            return None
        node = TreeNode(data['data'])
        node.left = to_tree(data['left'])
        node.right = to_tree(data['right'])
        return node

    return to_tree(json.loads(json_string))
