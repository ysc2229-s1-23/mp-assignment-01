class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_sublist(head: ListNode, p: int, q: int) -> ListNode:
    if not head or p == q:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(p - 1):
        prev = prev.next

    current = prev.next
    for _ in range(q - p):
        temp = current.next
        current.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next
