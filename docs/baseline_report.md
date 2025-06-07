# Baseline Model Report

This report summarizes the initial experiments on predicting reimbursement amounts.

## Setup

We evaluated two linear regression models using 1,000 public cases:

1. **Baseline** – uses the raw inputs:
   - `trip_duration_days`
   - `miles_traveled`
   - `total_receipts_amount`
2. **Engineered** – adds features inspired by the interview hints:
   - `miles_per_day`
   - `receipts_per_day`
   - `high_miles` (1 if miles_per_day > 180)
   - `high_receipts` (1 if receipts_per_day > 100)

Both models were evaluated with 5‑fold cross‑validation and mean absolute error (MAE).

## Results

Running `baseline.py` produced the following output:

```
Baseline MAE (5-fold CV): 176.45
Engineered MAE (5-fold CV): 161.61
```

The engineered features reduced the MAE slightly, indicating that mileage per day and spending patterns carry some predictive signal.

