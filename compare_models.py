"""Compare polynomial regression, k-NN, and rule-based models."""
import json
import math
import numpy as np

from rule_based import calculate_reimbursement

with open('public_cases.json') as f:
    cases = json.load(f)

# Build features for polynomial regression (degree 2)
X = []
y = []
for c in cases:
    td = float(c['input']['trip_duration_days'])
    mi = float(c['input']['miles_traveled'])
    re = float(c['input']['total_receipts_amount'])
    X.append([1.0, td, mi, re, td * td, mi * mi, re * re, td * mi, td * re, mi * re])
    y.append(float(c['expected_output']))
X = np.array(X)
y = np.array(y)

coeffs = np.linalg.lstsq(X, y, rcond=None)[0]
pred_poly = X.dot(coeffs)
mae_poly = float(np.mean(np.abs(pred_poly - y)))

# k-NN LOOCV (k=1)
train = [(c['input']['trip_duration_days'], c['input']['miles_traveled'],
          c['input']['total_receipts_amount'], c['expected_output']) for c in cases]

def knn_predict(dataset, td, miles, receipts, k=1):
    dists = []
    for dt, mi, re, out in dataset:
        d = math.sqrt(((td - dt)/12)**2 + ((miles - mi)/1000)**2 + ((receipts - re)/2000)**2)
        dists.append((d, out))
    dists.sort(key=lambda x: x[0])
    return dists[0][1] if k == 1 else sum(out/(d+1e-6) for d,out in dists[:k]) / sum(1/(d+1e-6) for d,_ in dists[:k])

mae_knn = 0.0
n = len(train)
for i in range(n):
    sub = train[:i] + train[i+1:]
    td, mi, re, exp = train[i]
    pred = knn_predict(sub, td, mi, re, k=1)
    mae_knn += abs(pred - exp)
mae_knn /= n

# Rule-based model
mae_rule = 0.0
for c in cases:
    td = c['input']['trip_duration_days']
    mi = c['input']['miles_traveled']
    re = c['input']['total_receipts_amount']
    exp = c['expected_output']
    pred = calculate_reimbursement(td, mi, re)
    mae_rule += abs(pred - exp)
mae_rule /= len(cases)

print(f"Polynomial MAE: {mae_poly:.2f}")
print(f"k-NN MAE: {mae_knn:.2f}")
print(f"Rule-based MAE: {mae_rule:.2f}")

best = min([
    ('Polynomial regression', mae_poly),
    ('k-NN (k=1)', mae_knn),
    ('Rule-based', mae_rule)
], key=lambda x: x[1])

print('\nBest model:', best[0])
