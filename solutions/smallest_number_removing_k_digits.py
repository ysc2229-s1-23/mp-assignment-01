def remove_k_digits(num: str, k: int) -> str:

    stack = []

    for digit in num:

        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    while k > 0:
        stack.pop()
        k -= 1

    smallest_num = ''.join(stack).lstrip('0')

    return smallest_num or '0'
