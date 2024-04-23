class Node:
    def __init__(self, data, left= None, right= None):
        self.data = data
        self.left = left
        self.right = right 

# Pre-order traversal
def pre_order(node):
    res = []
    if node:
        res = [node.data]   
        if node.left:
            res += pre_order(node.left)
        if node.right:
            res += pre_order(node.right)
    return res

# In-order traversal
def in_order(node):
    res = []
    if not node:
        return res
    if node.left:
        res += in_order(node.left)
    res.append(node.data)
    if node.right:
        res += in_order(node.right)
    return res

# Post-order traversal
def post_order(node):
    res = []
    if not node:
        return res
    if node.left:
        res += post_order(node.left)
    if node.right:
        res += post_order(node.right)
    res.append(node.data)
    return res
