import json, numpy as np, sys, math, statistics
with open('public_cases.json') as f:
    data=json.load(f)
X=[]
y=[]
for case in data:
    inp=case['input']
    X.append([1, inp['trip_duration_days'], inp['miles_traveled'], inp['total_receipts_amount']])
    y.append(case['expected_output'])
A=np.array(X)
b=np.array(y)
coeffs=np.linalg.lstsq(A,b,rcond=None)[0]
print('Coefficients', coeffs)
print('Baseline prediction formula:')
print('pred =', ' + '.join(f'{c:.4f}*f{i}' for i,c in enumerate(coeffs)))
mae=np.mean(np.abs(A.dot(coeffs)-b))
print('MAE', mae) 