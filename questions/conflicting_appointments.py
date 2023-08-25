"""
Problem: Conflicting Appointments

Description:
Given a list of intervals representing 'N' appointments, determine if a person can attend all the appointments without any overlaps. An overlap is considered if one appointment starts before the other one finishes.

Function Signature:
def can_attend_all_appointments(intervals: List[List[int]]) -> bool:

Inputs:
    - intervals (List[List[int]]): A list of intervals. Each interval is represented by a list of two integers - the start and end time.

Returns:
    - bool: Return True if a person can attend all the appointments without any conflicts. Otherwise, return False.

Examples:

1. Input: intervals = [[1,4], [2,5], [7,9]]
   Output: False
   Explanation: The first and the second appointment overlap.

2. Input: intervals = [[6,7], [2,4], [8,12]]
   Output: True
   Explanation: None of the appointments overlap.

3. Input: intervals = [[4,5], [2,3], [3,6]]
   Output: False
   Explanation: The last two appointments overlap.

Notes:
    - An appointment [a, b] is said to be conflicting with another appointment [c, d] if a < d and c < b.
    - Consider sorting the intervals based on start times and then checking for overlaps.

Tags:
    - Array
    - Sorting
    - Intervals
"""

from typing import List


def can_attend_all_appointments(intervals: List[List[int]]) -> bool:
    # TODO: Implement the function
    return False
