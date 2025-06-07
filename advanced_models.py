import json
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error

# Load data
with open('public_cases.json') as f:
    cases = json.load(f)

# Build feature matrix
X_raw = []
y = []
for c in cases:
    inp = c['input']
    td = float(inp['trip_duration_days'])
    mi = float(inp['miles_traveled'])
    re_amt = float(inp['total_receipts_amount'])
    mpd = mi / td
    rpd = re_amt / td
    X_raw.append([
        td,
        mi,
        re_amt,
        mpd,
        rpd,
        1.0 if td > 5 else 0.0,
        1.0 if mi > 300 else 0.0,
        1.0 if re_amt > 1000 else 0.0,
    ])
    y.append(float(c['expected_output']))
X_raw = np.array(X_raw)
y = np.array(y)

# Polynomial features degree 2
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X_raw)

# Cross-validation setup
kf = KFold(n_splits=5, shuffle=True, random_state=42)

poly_maes = []
knn_maes = []

for train_idx, test_idx in kf.split(X_poly):
    X_train, X_test = X_poly[train_idx], X_poly[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

    # Polynomial regression (linear model on polynomial features)
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    pred_lr = lr.predict(X_test)
    poly_maes.append(mean_absolute_error(y_test, pred_lr))

    # k-NN regression fallback
    knn = KNeighborsRegressor(n_neighbors=3, weights='distance')
    knn.fit(X_train, y_train)
    pred_knn = knn.predict(X_test)
    knn_maes.append(mean_absolute_error(y_test, pred_knn))

print('Polynomial Regression MAE (5-fold CV):', np.mean(poly_maes))
print('k-NN Regression MAE (5-fold CV):', np.mean(knn_maes))
