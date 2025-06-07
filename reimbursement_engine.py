coeffs = [-165.1388482652245, 88.17230215631075, 0.40695501110705506, 1.211676557393509, -2.5902746074702305, 3.526925506668234e-05, -0.00027852019708561864, 0.014510187774824712, -0.008909396689364702, -0.00011392118366372584]

def predict(trip_duration_days, miles_traveled, total_receipts_amount):
    td = float(trip_duration_days)
    mi = float(miles_traveled)
    re = float(total_receipts_amount)
    feats = [
        1.0,
        td,
        mi,
        re,
        td * td,
        mi * mi,
        re * re,
        td * mi,
        td * re,
        mi * re,
    ]
    val = sum(c * f for c, f in zip(coeffs, feats))
    return round(val, 2)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        raise SystemExit("Usage: reimbursement_engine.py td days miles receipts")
    print(predict(sys.argv[1], sys.argv[2], sys.argv[3]))
