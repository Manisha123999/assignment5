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

    def find(self, value):
        return self._find_recursive(self.root, value)

    def _find_recursive(self, current, value):
        if current is None or current.value == value:
            return current

        if value < current.value:
            return self._find_recursive(current.left, value)
        else:
            return self._find_recursive(current.right, value)


# Example usage
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

node = bst.find(4)
print(node)  # Output: Node(4)

node = bst.find(9)
print(node)  # Output: None