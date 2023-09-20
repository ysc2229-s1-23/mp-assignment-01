from typing import List


def search_triplets(arr: List[int]) -> List[List[int]]:
    arr.sort()
    triplets = []

    for i in range(len(arr)):

        if i > 0 and arr[i] == arr[i-1]:
            continue

        left, right = i + 1, len(arr) - 1
        while left < right:
            triplet_sum = arr[i] + arr[left] + arr[right]
            if triplet_sum == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1

                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif triplet_sum < 0:
                left += 1
            else:
                right -= 1

    return triplets
