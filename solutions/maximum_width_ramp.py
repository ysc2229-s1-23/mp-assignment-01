from typing import List


def maxWidthRamp(nums: List[int]) -> int:
    stack = []
    max_width = 0

    for i, num in enumerate(nums):
        if not stack or nums[stack[-1]] > num:
            stack.append(i)

    for j in reversed(range(len(nums))):
        while stack and nums[stack[-1]] <= nums[j]:
            max_width = max(max_width, j - stack.pop())

    return max_width
