class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def is_palindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev, curr = None, slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    first_half, second_half = head, prev
    is_palindrome = True
    while second_half:
        if first_half.value != second_half.value:
            is_palindrome = False
            break
        first_half = first_half.next
        second_half = second_half.next

    curr, prev = prev, None
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    return is_palindrome
