from typing import List


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def zigzag_level_order_traversal(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = [root]
    left_to_right = True 

    while queue:
        level_size = len(queue)
        current_level = []

        for i in range(level_size):
            current_node = queue.pop(0)

            if left_to_right:
                current_level.append(current_node.value)
            else:
                current_level.insert(0, current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(current_level)
        left_to_right = not left_to_right

    return result
