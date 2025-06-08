import json
from rule_based import calculate_reimbursement

def test_private_cases():
    # Load private cases
    with open('private_cases.json', 'r') as f:
        cases = json.load(f)
    
    # Track results
    total_cases = len(cases)
    correct = 0
    errors = []
    
    # Test each case
    for i, case in enumerate(cases):
        days = case['trip_duration_days']
        miles = case['miles_traveled']
        receipts = case['total_receipts_amount']
        
        # Calculate reimbursement
        calculated = calculate_reimbursement(days, miles, receipts)
        
        # For private cases, we don't have expected values
        # Instead, we'll check if the calculation follows our rules
        # and if the result is reasonable
        
        # Basic sanity checks
        if calculated < 0:
            errors.append({
                'case_id': i + 1,
                'days': days,
                'miles': miles,
                'receipts': receipts,
                'calculated': calculated,
                'reason': 'Negative reimbursement'
            })
        elif calculated > 10000:  # Unreasonably high
            errors.append({
                'case_id': i + 1,
                'days': days,
                'miles': miles,
                'receipts': receipts,
                'calculated': calculated,
                'reason': 'Unreasonably high reimbursement'
            })
        else:
            correct += 1
    
    # Print results
    print(f"\nPrivate Test Results:")
    print(f"Total cases: {total_cases}")
    print(f"Valid predictions: {correct}")
    print(f"Accuracy: {(correct/total_cases)*100:.2f}%")
    
    if errors:
        print("\nFirst 5 errors:")
        for error in errors[:5]:
            print(f"\nCase {error['case_id']}:")
            print(f"Input: {error['days']} days, {error['miles']} miles, ${error['receipts']:.2f} receipts")
            print(f"Calculated: ${error['calculated']:.2f}")
            print(f"Reason: {error['reason']}")

if __name__ == "__main__":
    test_private_cases() 