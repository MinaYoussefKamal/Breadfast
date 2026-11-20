"""Tests for the example thresholds; update to the real Kata specification."""
import pytest
from week5.grades import calculate_grade

@pytest.mark.parametrize(("score", "expected"), [
    (100, "A"), (90, "A"), (89, "B"), (80, "B"), (79, "C"),
    (70, "C"), (69, "D"), (60, "D"), (59, "F"), (0, "F"),
])
def test_calculate_grade_boundaries(score, expected):
    assert calculate_grade(score) == expected
