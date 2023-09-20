from typing import List


def two_sum(arr: List[int], target: int) -> List[int]:
    left, right = 0, len(arr) - 1
    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]

        if target > current_sum:
            left += 1
        else:
            right -= 1
    return [-1, -1]
