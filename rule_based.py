import math

def calculate_reimbursement(trip_duration_days, miles_traveled, total_receipts_amount):
    """Pure rule-based reimbursement calculation with balanced rates."""
    td = int(trip_duration_days)
    miles = float(miles_traveled)
    receipts = float(total_receipts_amount)

    reimbursement = 0.0

    # --- 1. Base per-day rate ---
    reimbursement += round(td * 85.0, 2)  # Balanced base rate

    # --- 2. 5-day trip bonus ---
    if td == 5:
        reimbursement += 50.0

    # --- 3. Mileage reimbursement ---
    first_100_miles = min(miles, 100)
    above_100_miles = min(max(miles - 100, 0), 300)  # Cap at 300 miles
    mileage_amt = round(0.58 * first_100_miles + 0.05 * above_100_miles, 2)  # Balanced rate
    reimbursement += mileage_amt

    # --- 4. Receipt reimbursement ---
    first_100_receipts = min(receipts, 100)
    above_100_receipts = min(max(receipts - 100, 0), 300)  # Cap at $300
    receipt_amt = round(0.8 * first_100_receipts + 0.05 * above_100_receipts, 2)  # Balanced rate
    reimbursement += receipt_amt

    # --- 5. Efficiency bonus ---
    miles_per_day = miles / td if td > 0 else 0
    if miles_per_day > 100:
        efficiency_bonus = min((miles_per_day - 100) * 0.05 * td, 100.0)  # Capped at $100
        efficiency_bonus = round(efficiency_bonus, 2)
        reimbursement += efficiency_bonus

    # --- 6. Special rounding/receipt cents bonus ---
    cents = int(round(receipts * 100)) % 100
    if cents in (49, 99):
        reimbursement += 5.0

    # --- 7. Final rounding ---
    return round(reimbursement, 2)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python rule_based.py <days> <miles> <receipts>")
    else:
        days, miles, receipts = sys.argv[1:4]
        print(calculate_reimbursement(float(days), float(miles), float(receipts)))
