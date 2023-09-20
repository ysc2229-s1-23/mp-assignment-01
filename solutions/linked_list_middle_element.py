class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle(head):
    slow = head
    fast = head
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow
