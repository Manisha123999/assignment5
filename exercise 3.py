class BST:
    # Existing code for Node and BST classes...

    def _detach_node(self, node):
        if node is None:
            return

        # Helper function to find the parent of a node
        def find_parent(root, target):
            if root is None:
                return None
            elif root.left == target or root.right == target:
                return root
            elif target.value < root.value:
                return find_parent(root.left, target)
            else:
                return find_parent(root.right, target)

        # Helper function to find the minimum node in a subtree
        def find_minimum_node(subtree_root):
            current = subtree_root
            while current.left:
                current = current.left
            return current

        # Case: Node to detach is the root
        if node == self.root:
            if node.left is None and node.right is None:
                self.root = None
            elif node.left and node.right:
                raise ValueError("Cannot detach node with two children from BST")
            elif node.left:
                self.root = node.left
            else:
                self.root = node.right
            return

        # Find parent of the node to detach
        parent = find_parent(self.root, node)

        # Case: Node to detach is a leaf node
        if node.left is None and node.right is None:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
        # Case: Node to detach has one child
        elif node.left is None:
            if parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right
        elif node.right is None:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
        # Case: Node to detach has two children
        else:
            # Find the minimum node in the right subtree
            min_node = find_minimum_node(node.right)
            # Replace the value of the node to detach with the value of the minimum node
            node.value = min_node.value
            # Detach the minimum node
            self._detach_node(min_node)