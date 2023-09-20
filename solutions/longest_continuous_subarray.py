from collections import deque
from typing import List


def longest_subarray(nums: List[int], limit: int) -> int:
    max_deque, min_deque = deque(), deque()
    left, ans = 0, 0

    for right in range(len(nums)):
        while max_deque and nums[right] > nums[max_deque[-1]]:
            max_deque.pop()
        while min_deque and nums[right] < nums[min_deque[-1]]:
            min_deque.pop()

        max_deque.append(right)
        min_deque.append(right)

        while nums[max_deque[0]] - nums[min_deque[0]] > limit:
            if max_deque[0] < min_deque[0]:
                left = max_deque.popleft() + 1
            else:
                left = min_deque.popleft() + 1

        ans = max(ans, right - left + 1)

    return ans
