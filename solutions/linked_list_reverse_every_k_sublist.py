class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_every_k_elements(head: ListNode, k: int) -> ListNode:
    if not head or k == 1:
        return head

    new_head, prev_tail = None, None
    current = head

    while current:
        segment_start = current

        i = 0
        while current and i < k:
            current = current.next
            i += 1

        reversed_start, reversed_end = reverse_segment(segment_start, i)

        if not new_head:
            new_head = reversed_start
        if prev_tail:
            prev_tail.next = reversed_start

        reversed_end.next = current

        prev_tail = reversed_end

    return new_head if new_head else head


def reverse_segment(start: ListNode, k: int) -> (ListNode, ListNode):
    prev = None
    current = start
    while k > 0:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        k -= 1

    return prev, start
