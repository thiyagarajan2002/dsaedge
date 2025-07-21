
def visualize_tree(root):
    """Prints a simple visualization of the tree."""
    if not root:
        print("Tree is empty")
        return

    def print_tree(node, prefix="", is_left=True):
        if not node:
            return

        if node.right:
            print_tree(node.right, prefix + ("|   " if is_left else "    "), False)

        print(prefix + ("`-- " if is_left else "-- ") + str(node.data))

        if node.left:
            print_tree(node.left, prefix + ("    " if is_left else "|   "), True)

    print_tree(root)
