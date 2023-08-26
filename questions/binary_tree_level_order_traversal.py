"""
Problem: Level-by-Level Traversal of Binary Tree

Description:
Given a binary tree, the task is to populate an array to represent its level-by-level traversal. Populate the values of all nodes of each level from left to right in separate sub-arrays.

Function Signature:
def level_order_traversal(root: TreeNode) -> List[List[int]]:

Inputs:
    - root (TreeNode): The root node of the binary tree. The TreeNode is defined as:
        class TreeNode:
            def __init__(self, value=0, left=None, right=None):
                self.value = value
                self.left = left
                self.right = right

Returns:
    - List[List[int]]: A list where each inner list contains the values of the nodes for each level from left to right.

Examples:

1. Input:
        Tree Structure:
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
   Output: [[1], [2, 3], [4, 5, 6, 7]]

2. Input:
        Tree Structure:
           12
         /    \
        7     1
       /     / \
      9     10  5
   Output: [[12], [7, 1], [9, 10, 5]]

Notes:
    - Consider using a queue to process nodes at each level.
    - At the start of each level, record the current size of the queue. This size represents the number of nodes at the current level.
    - Process nodes of each level using a loop and pop nodes from the front of the queue, adding their children (if they have any) to the back of the queue.

Tags:
    - Trees
    - Queue
"""

from typing import List


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def level_order_traversal(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    # TODO: Implement the BFS algorithm to populate the result list
    result = []
    # ...
    return result
