import json
from rule_based import calculate_reimbursement

def test_synthetic_cases():
    # Load synthetic cases and expected results
    with open('synthetic_cases.json', 'r') as f:
        cases = json.load(f)
    with open('synthetic_expected.json', 'r') as f:
        expected = json.load(f)
    
    # Track results
    total_cases = len(cases)
    correct = 0
    errors = []
    
    # Test each case
    for i, case in enumerate(cases):
        input_data = case['input']
        days = input_data['trip_duration_days']
        miles = input_data['miles_traveled']
        receipts = input_data['total_receipts_amount']
        
        # Calculate reimbursement
        calculated = calculate_reimbursement(days, miles, receipts)
        expected_amt = expected[i]  # Use integer index
        
        # Check if correct
        if abs(calculated - expected_amt) < 0.01:  # Allow for small floating point differences
            correct += 1
        else:
            errors.append({
                'case_id': i + 1,
                'days': days,
                'miles': miles,
                'receipts': receipts,
                'calculated': calculated,
                'expected': expected_amt,
                'difference': calculated - expected_amt
            })
    
    # Print results
    print(f"\nSynthetic Test Results:")
    print(f"Total cases: {total_cases}")
    print(f"Correct predictions: {correct}")
    print(f"Accuracy: {(correct/total_cases)*100:.2f}%")
    
    if errors:
        print("\nFirst 5 errors:")
        for error in errors[:5]:
            print(f"\nCase {error['case_id']}:")
            print(f"Input: {error['days']} days, {error['miles']} miles, ${error['receipts']:.2f} receipts")
            print(f"Calculated: ${error['calculated']:.2f}")
            print(f"Expected: ${error['expected']:.2f}")
            print(f"Difference: ${error['difference']:.2f}")

if __name__ == "__main__":
    test_synthetic_cases() 