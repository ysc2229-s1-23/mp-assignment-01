from typing import List
from collections import deque


def count_continuous_subarrays(nums: List[int]) -> int:
    start = 0
    end = 0
    count = 0
    q = deque()
    max_q = deque()
    min_q = deque()

    while end < len(nums):

        q.append(nums[end])

        while max_q and max_q[-1] < nums[end]:
            max_q.pop()
        max_q.append(nums[end])

        while min_q and min_q[-1] > nums[end]:
            min_q.pop()
        min_q.append(nums[end])

        while max_q[0] - min_q[0] > 2:
            if q[0] == max_q[0]:
                max_q.popleft()
            if q[0] == min_q[0]:
                min_q.popleft()
            q.popleft()
            start += 1

        count += end - start + 1
        end += 1

    return count
