class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def find_maximum(self):
        if self.root is None:
            return None

        current = self.root
        while current.right is not None:
            current = current.right

        return current

    def find_minimum(self):
        if self.root is None:
            return None

        current = self.root
        while current.left is not None:
            current = current.left

        return current


# Example usage
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

max_node = bst.find_maximum()
print(max_node)  # Output: Node(8)

min_node = bst.find_minimum()
print(min_node)  # Output: Node(2)