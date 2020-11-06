class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"


def bst_numbers_sum(root, num=0):
    if root == None:
        return 0
    num = (num*10 + root.value)

    if root.left is None and root.right is None:
        return num

    return bst_numbers_sum(root.left, num) + bst_numbers_sum(root.right, num)


n5 = Node(5)
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  / \
# 4   5
#

print(bst_numbers_sum(n1))
# 262
# Explanation: 124 + 125 + 13 = 262
