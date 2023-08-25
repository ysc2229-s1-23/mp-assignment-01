"""
Problem: Remove Nodes with Greater Value to the Right in a Singly Linked List

Description:
Given a singly linked list, remove any node that has a node with a greater value to its right. 
Return the head of the modified list. Ensure your algorithm does not modify the original linked list 
after the function is executed.

Function Signature:
def modify_linked_list(head: ListNode) -> ListNode:

Inputs:
    - head (ListNode): The head node of the singly linked list, with each node containing an integer value.

Returns:
    - ListNode: The head node of the modified list.

Notes:
    - The linked list will have at least one element.
    - Do not return a new linked list. Modify the given linked list in-place and return its head.

Examples:

1. Input: 5 -> 3 -> 7 -> 4 -> 2 -> 1
   Output: 7 -> 4 -> 2 -> 1
   Explanation: 5 and 3 are removed as they have nodes with larger values to their right.
   
2. Input: 1 -> 2 -> 3 -> 4 -> 5
   Output: 5
   Explanation: 1, 2, 3, and 4 are removed as they have nodes with larger values to their right.
   
3. Input: 5 -> 4 -> 3 -> 2 -> 1
   Output: 5 -> 4 -> 3 -> 2 -> 1
   Explanation: None of the nodes are removed as none of them have nodes with larger values to their right.

Hints:
    - Consider iterating the list from right to left (reverse order) to efficiently determine which nodes to remove.
    - Keep track of the maximum value observed so far during iteration to decide if a node should be removed.

Tags:
    - LinkedList
    - Stack

"""

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def modify_linked_list(head: ListNode) -> ListNode:
    # TODO: Implement the function
    return head
