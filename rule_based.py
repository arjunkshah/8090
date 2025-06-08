import math

# Rule-based reimbursement calculation derived from interview hints.

def calculate_reimbursement(trip_duration_days, miles_traveled, total_receipts_amount):
    """Compute reimbursement using explicit rules."""
    td = float(trip_duration_days)
    miles = float(miles_traveled)
    receipts = float(total_receipts_amount)

    # Base daily rate
    amount = 100.0 * td

    # Bonus for exactly 5 day trips (mentioned by accounting)
    if td == 5:
        amount += 50.0

    # Mileage reimbursement with tiered rates
    first_100 = min(miles, 100)
    extra = max(miles - 100, 0)
    mileage_amt = 0.58 * first_100 + 0.35 * extra
    amount += mileage_amt

    # Efficiency bonus for high mileage per day
    if td > 0 and (miles / td) > 150:
        amount += 0.10 * mileage_amt

    # Receipt reimbursement with diminishing returns
    if receipts < 50:
        receipt_amt = receipts * 0.5
    elif receipts <= 800:
        receipt_amt = receipts * 0.9
    else:
        receipt_amt = 720 + (receipts - 800) * 0.25

    # Rounding bug: extra for receipts ending in 49 or 99 cents
    cents = int(round(receipts * 100)) % 100
    if cents in (49, 99):
        receipt_amt += 5.0

    amount += receipt_amt
    return round(amount, 2)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python rule_based.py <days> <miles> <receipts>")
    else:
        days, miles, receipts = sys.argv[1:4]
        print(calculate_reimbursement(float(days), float(miles), float(receipts)))
