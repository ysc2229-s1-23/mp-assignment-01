from typing import List


def search_quadruplets(arr: List[int], target: int) -> List[List[int]]:
    arr.sort()
    quadruplets = []
    for i in range(0, len(arr)-3):

        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr)-2):

            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            search_pairs(arr, target, i, j, quadruplets)
    return quadruplets


def search_pairs(arr: List[int], target_sum: int, first: int, second: int, quadruplets: List[List[int]]):
    left = second + 1
    right = len(arr) - 1
    while (left < right):
        quad_sum = arr[first] + arr[second] + arr[left] + arr[right]
        if quad_sum == target_sum:
            quadruplets.append(
                [arr[first], arr[second], arr[left], arr[right]])
            left += 1
            right -= 1
            while (left < right and arr[left] == arr[left - 1]):
                left += 1
            while (left < right and arr[right] == arr[right + 1]):
                right -= 1
        elif quad_sum < target_sum:
            left += 1
        else:
            right -= 1
