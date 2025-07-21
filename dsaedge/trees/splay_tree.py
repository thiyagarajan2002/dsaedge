
class SplayNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _splay(self, x):
        while x.parent:
            if not x.parent.parent:
                if x == x.parent.left:
                    # Zig
                    self._right_rotate(x.parent)
                else:
                    # Zag
                    self._left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                # Zig-Zig
                self._right_rotate(x.parent.parent)
                self._right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                # Zag-Zag
                self._left_rotate(x.parent.parent)
                self._left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                # Zig-Zag
                self._left_rotate(x.parent)
                self._right_rotate(x.parent)
            else:
                # Zag-Zig
                self._right_rotate(x.parent)
                self._left_rotate(x.parent)

    def insert(self, data):
        if not self.root:
            self.root = SplayNode(data)
            return

        node = self.root
        parent = None
        while node:
            parent = node
            if data < node.data:
                node = node.left
            else:
                node = node.right
        
        new_node = SplayNode(data)
        new_node.parent = parent
        if data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        
        self._splay(new_node)

    def search(self, data):
        node = self.root
        while node:
            if data == node.data:
                self._splay(node)
                return node
            elif data < node.data:
                node = node.left
            else:
                node = node.right
        return None
