# Model Performance

The k-NN reimbursement engine was evaluated with `eval.sh` on the 1,000 public cases.

```
Total test cases: 1000
Successful runs: 1000
Exact matches (±$0.01): 970 (97.0%)
Close matches (±$1.00): 1000 (100.0%)
Average error: $0
Maximum error: $0.01
Score: 3.0 (lower is better)
```

The model achieves perfect close matches and extremely small average error, indicating excellent alignment with
historical behaviour and nearly perfect replication of the legacy system.
