# Model Comparison

We evaluated two advanced models on the provided `public_cases.json` data using five-fold cross validation. Engineered features were derived from the raw inputs:

- trip duration, miles traveled and receipt total
- miles per day and receipts per day
- flags for long trips (>5 days), high mileage (>300 miles) and high receipts (>\$1000)

A second-degree polynomial basis was applied to these features for the regression model. The k‑NN regressor used distance weighting with `k=3`.

| Model | MAE |
|-------|----:|
| Polynomial Regression | 90.26 |
| k‑NN Regression | 113.94 |

The polynomial regression on engineered features performed best, achieving a lower mean absolute error than the k‑NN fallback model.
