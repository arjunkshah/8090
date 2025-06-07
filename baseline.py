import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error

with open('public_cases.json') as f:
    data = json.load(f)

# Prepare baseline feature matrix (3 raw inputs)
X_baseline = []
y = []
for case in data:
    inp = case['input']
    X_baseline.append([
        inp['trip_duration_days'],
        inp['miles_traveled'],
        inp['total_receipts_amount'],
    ])
    y.append(case['expected_output'])
X_baseline = np.array(X_baseline)
y = np.array(y)

# Additional engineered features
X_engineered = []
for case in data:
    inp = case['input']
    td = inp['trip_duration_days']
    miles = inp['miles_traveled']
    receipts = inp['total_receipts_amount']
    miles_per_day = miles / td
    receipts_per_day = receipts / td
    high_miles = 1.0 if miles_per_day > 180 else 0.0
    high_receipts = 1.0 if receipts_per_day > 100 else 0.0
    X_engineered.append([
        td,
        miles,
        receipts,
        miles_per_day,
        receipts_per_day,
        high_miles,
        high_receipts,
    ])
X_engineered = np.array(X_engineered)

kf = KFold(n_splits=5, shuffle=True, random_state=42)

mae_baseline = []
mae_engineered = []
for train_idx, test_idx in kf.split(X_baseline):
    model = LinearRegression()
    model.fit(X_baseline[train_idx], y[train_idx])
    pred = model.predict(X_baseline[test_idx])
    mae_baseline.append(mean_absolute_error(y[test_idx], pred))

    model2 = LinearRegression()
    model2.fit(X_engineered[train_idx], y[train_idx])
    pred2 = model2.predict(X_engineered[test_idx])
    mae_engineered.append(mean_absolute_error(y[test_idx], pred2))

print('Baseline MAE (5-fold CV):', np.mean(mae_baseline))
print('Engineered MAE (5-fold CV):', np.mean(mae_engineered))
