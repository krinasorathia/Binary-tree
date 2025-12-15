from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)

    q = deque([root])
    while q:
        temp = q.popleft()

        if temp.left is None:
            temp.left = Node(data)
            break
        else:
            q.append(temp.left)

        if temp.right is None:
            temp.right = Node(data)
            break
        else:
            q.append(temp.right)

    return root

def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    return search(root.left, key) or search(root.right, key)

def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

if __name__ == "__main__":
    root = None
    values = [10, 20, 30, 40, 50]
    for v in values:
        root = insert(root, v)

    print("Search 30:", search(root, 30))
    print("Height of tree:", height(root))
    print("Total nodes:", count_nodes(root))
    print("Leaf nodes:", count_leaf_nodes(root))
