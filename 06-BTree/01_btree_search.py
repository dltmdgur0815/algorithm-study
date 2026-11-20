class Node:
    def __init__(self, keys, children=None):
        self.keys = keys
        self.children = children if children is not None else []

def make_tree():

    left = Node([5, 12, 18])
    middle = Node([28, 35])
    right = Node([48, 56, 63])
    return Node([22, 41], [left, middle, right])

def search(root, target):
    path = []
    current = root
    while current is not None:
        path.append(current.keys.copy())
        index = 0
        while index < len(current.keys) and target > current.keys[index]:
            index += 1
        if index < len(current.keys) and target == current.keys[index]:
            return True, path
        if not current.children:
            return False, path
        current = current.children[index]
    return False, path
