class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def target_sum_bst(root, target):
    it1, it2 = [], []

    itr = root
    while (itr != None):
        it1.append(itr)
        itr = itr.left

    itr = root
    while (itr != None):
        it2.append(itr)
        itr = itr.right

    while (it1[-1] != it2[-1]):

        v1 = it1[-1].value
        v2 = it2[-1].value

        if (v1 + v2 == target):
            return True

        if (v1 + v2 < target):
            itr = it1[-1].right
            del it1[-1]

            while (itr != None):
                it1.append(itr)
                itr = itr.left

        else:
            itr = it2[-1].left
            del it2[-1]

            while (itr != None):
                it2.append(itr)
                itr = itr.right

    return False

    #      1
    #    /   \
    #   2     3
    #    \     \
    #     6     4
n6 = Node(6)
n4 = Node(4)
n3 = Node(3, None, n4)
n2 = Node(2, None, n6)
n1 = Node(1, n2, n3)

print(target_sum_bst(n1, 9))
# True
# Path from 1 -> 2 -> 6
