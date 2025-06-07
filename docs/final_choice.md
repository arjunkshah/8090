# Final Model Choice

After experimenting with several approaches, the following mean absolute errors (MAE) were observed on the 1,000 public test cases:

| Model | MAE |
|-------|-----|
| Polynomial regression (degree 2) | ~109.86 |
| k-NN regression (k=1) | ~108.62 |
| Rule-based system | ~339.43 |

The rule-based system was derived from high-confidence hypotheses in `INTERVIEWS.md` (base per diem, five‑day bonus, mileage tiers, receipt diminishing returns and a rounding quirk). While these rules capture some qualitative behaviors, the error remained much higher than the machine‑learned models.

Between the machine‑learned options, k‑NN with `k=1` provided the lowest MAE on the public data, slightly outperforming the polynomial regression. For now the k‑NN approach is selected as the best approximation of the legacy system.
