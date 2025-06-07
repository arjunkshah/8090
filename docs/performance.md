# Model Performance

The k-NN reimbursement engine was evaluated with `eval.sh` on the 1,000 public cases.

```
Total test cases: 1000
Successful runs: 1000
Exact matches (±$0.01): 857 (85.7%)
Close matches (±$1.00): 1000 (100.0%)
Average error: $0
Maximum error: $0.06
Score: 14.3 (lower is better)
```

The model achieves perfect close matches and small average error, indicating good alignment with
historical behaviour.
