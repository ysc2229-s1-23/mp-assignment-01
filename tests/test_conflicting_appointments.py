"""
Test cases for can_attend_all_appointments
"""

from questions.conflicting_appointments import can_attend_all_appointments


def test_can_attend_all_appointments():
    """
    Tests for can_attend_all_appointments
    """

    assert not can_attend_all_appointments(
        [[1, 4], [2, 5], [7, 9]]), "Test Case 1 Failed"

    assert can_attend_all_appointments(
        [[6, 7], [2, 4], [8, 12]]), "Test Case 2 Failed"

    assert not can_attend_all_appointments(
        [[4, 5], [2, 3], [3, 6]]), "Test Case 3 Failed"

    assert can_attend_all_appointments([]), "Test Case 4 Failed"

    assert can_attend_all_appointments([[2, 5]]), "Test Case 5 Failed"

    assert can_attend_all_appointments(
        [[1, 3], [3, 5], [5, 7]]), "Test Case 6 Failed"

    assert not can_attend_all_appointments(
        [[1, 10], [2, 5], [3, 6]]), "Test Case 7 Failed"

    assert can_attend_all_appointments(
        [[8, 12], [2, 4], [6, 7]]), "Test Case 8 Failed"

    assert not can_attend_all_appointments(
        [[8, 12], [10, 15], [6, 7]]), "Test Case 9 Failed"

    assert not can_attend_all_appointments(
        [[1, 3], [1, 5], [6, 8]]), "Test Case 10 Failed"
