class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"


'''
#############################
##### Dynamic Solution ######
#############################
'''


def flatten_bst(root):
    # Check if the node is leaf or not
    if root.left == None and root.right == None:
        return root
    # If only right child is avaliable
    elif root.left == None:
        root.right = flatten_bst(root.right)
        return root
    # If only left child is avaliable swap it with right child and call recurssion
    elif root.right == None:
        root.right = root.left
        root.left = None
        root.right = flatten_bst(root.right)
        return root
    else:
        temp_Left = root.left
        temp_Right = root.right
        # Finding right end of left child
        while temp_Left.right != None:
            temp_Left = temp_Left.right

        temp_Left.right = temp_Right
        root.right = temp_Left
        root.left = None

        root.right = flatten_bst(root.right)
        return root


'''
#############################
##### Static Solution ######
#############################
'''


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
    root.right.right.right.right = root.right.right.right.left
    root.right.right.right.left = None


n5 = Node(5)
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n5)
n1 = Node(1, n2, n3)

flatten_bst(n1)
print(n1)
