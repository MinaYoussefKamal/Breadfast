"""Characterization tests for the example fee policy, not the missing original Kata."""
import pytest
from week5.fees import calculate_fee

@pytest.mark.parametrize(("amount", "rate", "expected"), [
    (0, 0.05, 0.00), (10, 0.05, 0.50), (100, 0.05, 5.00),
    (12.5, 0.10, 1.25),
])
def test_calculate_fee(amount, rate, expected):
    assert calculate_fee(amount, rate) == expected

@pytest.mark.parametrize(("amount", "rate"), [(-1, 0.05), (10, -0.01)])
def test_calculate_fee_rejects_negative_inputs(amount, rate):
    with pytest.raises(ValueError):
        calculate_fee(amount, rate)
