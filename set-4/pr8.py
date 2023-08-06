# 8. **Invert Binary Tree**: Invert a binary tree (mirroring it).
#     - *Input*: A binary tree
#     - *Output*: Inverted binary tree


# To invert a binary tree (mirror it), you can perform a simple tree traversal and swap the left and right children of each node. Here's a Python function to invert a binary tree:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if root is None:
        return None

    # Swap left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root

# Test the function
# Example binary tree:     1                 Inverted binary tree:    1
#                        /   \                                     /   \
#                       2     3                                   3     2
#                      / \   / \                                 / \   / \
#                     4   5 6   7                               7   6 5   4


# Create the example binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Invert the binary tree
inverted_tree = invert_tree(root)

# Helper function to print the binary tree in level order


def print_tree(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


print_tree(inverted_tree)
