class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"


def flatten_bst(root):
    # Save the whole right sub tree in the variable
    temp = root.right
    # over write the right aub tree with left sub tree
    root.right = root.left
    # Delete th eleft sub tree
    root.left = None
    # Now save the left sub tree to the right sub tree
    root.right.right = root.right.left
    # delete the left sub tree
    root.right.left = None
    # save the whole right sub tree in the right most node
    root.right.right.right = temp


n5 = Node(5)
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n5)
n1 = Node(1, n2, n3)

flatten_bst(n1)
print(n1)
