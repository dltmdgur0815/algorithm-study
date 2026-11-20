class Node:
    def __init__(self, number):
        self.number = number
        self.left = None
        self.right = None

def insert(root, number):
    if root is None:
        return Node(number)
    current = root
    while True:
        if number == current.number:
            return root
        if number < current.number:
            if current.left is None:
                current.left = Node(number)
                return root
            current = current.left
        else:
            if current.right is None:
                current.right = Node(number)
                return root
            current = current.right

def search(root, number):
    current = root
    while current is not None:
        if number == current.number:
            return True
        if number < current.number:
            current = current.left
        else:
            current = current.right
    return False

def inorder(root):
    result = []
    stack = []
    current = root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.number)
        current = current.right
    return result
