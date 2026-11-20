"""Example refactored fee calculation; replace with the specified fee policy."""
def calculate_fee(amount, rate=0.05):
    if amount < 0:
        raise ValueError("amount must not be negative")
    if rate < 0:
        raise ValueError("rate must not be negative")
    return round(amount * rate, 2)
