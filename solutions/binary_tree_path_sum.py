from typing import List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def has_path_sum(root: TreeNode, sum: int) -> bool:
    if not root:
        return False
    
    # If it's a leaf node, check if the remaining sum matches the leaf's value
    if not root.left and not root.right:
        return root.value == sum
    
    # Recursively check the left and right subtrees
    return (has_path_sum(root.left, sum - root.value) or has_path_sum(root.right, sum - root.value))