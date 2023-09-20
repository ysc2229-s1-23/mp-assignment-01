def remove_adjacent_dups(s: str) -> str:
    stack = []
    count_stack = []

    for char in s:
        if not stack or stack[-1] != char:
            stack.append(char)
            count_stack.append(1)
        else:
            count_stack[-1] += 1

        while count_stack and count_stack[-1] >= 2:
            stack.pop()
            count_stack.pop()

    return ''.join(stack)
