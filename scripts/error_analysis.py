import json
import subprocess

with open('public_cases.json') as f:
    cases = json.load(f)

results = []
for i, case in enumerate(cases):
    td = str(case['input']['trip_duration_days'])
    mi = str(case['input']['miles_traveled'])
    re = str(case['input']['total_receipts_amount'])
    expected = float(case['expected_output'])
    # Call the current model
    proc = subprocess.run(['python3', 'reimbursement_engine.py', td, mi, re], capture_output=True, text=True)
    try:
        pred = float(proc.stdout.strip())
    except Exception:
        pred = None
    error = abs(pred - expected) if pred is not None else None
    results.append({
        'index': i,
        'input': (td, mi, re),
        'expected': expected,
        'pred': pred,
        'error': error
    })

# Sort by error descending
results = [r for r in results if r['error'] is not None]
results.sort(key=lambda r: -r['error'])

print('Top 20 largest errors:')
for r in results[:20]:
    print(f"Case {r['index']}: input={r['input']} expected={r['expected']} pred={r['pred']} error={r['error']:.4f}")

# Print summary
exact = sum(1 for r in results if r['error'] < 0.01)
close = sum(1 for r in results if r['error'] < 1.0)
print(f"\nExact matches (<$0.01): {exact}/{len(results)}")
print(f"Close matches (<$1.00): {close}/{len(results)}")
print(f"Max error: {results[0]['error']:.4f}")
print(f"Mean absolute error: {sum(r['error'] for r in results)/len(results):.4f}") 