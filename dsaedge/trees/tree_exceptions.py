
class TreeError(Exception):
    """Base class for other exceptions in this module."""
    pass

class NodeNotFoundError(TreeError):
    """Raised when a node is not found in the tree."""
    pass

class InvalidOperationError(TreeError):
    """Raised when an invalid operation is performed on the tree."""
    pass

class TreeEmptyError(TreeError):
    """Raised when an operation is performed on an empty tree."""
    pass
