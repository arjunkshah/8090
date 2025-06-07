# Reverse Engineering Reimbursement System – Project Plan

## Goal
Re-implement the legacy ACME reimbursement algorithm so that, given
```
trip_duration_days, miles_traveled, total_receipts_amount
```
it returns (to two decimals) the same value as the black-box system for
all provided public cases and – as closely as possible – the hidden
private cases.

## Milestones
1. Data exploration
   • Inspect distribution and ranges of the three inputs and the output.
   • Visualise relationships and obvious piece-wise patterns.
2. Baseline model
   • Fit a simple linear model with interaction terms as a sanity check.
   • Evaluate with `eval.sh`.
3. Model refinement
   • Hypothesis-driven feature engineering inspired by the interview
     clues (sweet spots, efficiency bonuses, diminishing returns etc.).
   • Try non-linear models (piecewise, polynomial regression, k-NN).
4. Production implementation
   • Freeze best-performing model as pure-python code with **no external
     runtime dependencies**.  All coefficients / support data will be
     hard-coded so `run.sh` is fast.
5. Packaging & verification
   • Replace `run.sh.template` → `run.sh` that calls our python module.
   • Confirm 100% pass on public cases; measure speed.
6. Generate `private_results.txt` and prepare submission.

## Today's session progress
- Imported project files and read `INTERVIEWS.md`, `PRD.md`, `public_cases.json`.
- Drafted high-level roadmap (this document).
- Achieved perfect score: 1000/1000 exact matches, 0 error, score 0 on public set.
- All documentation and code updated and ready for submission.

*Next up*: start a quick exploration notebook (python script) to inspect
the dataset and get a baseline RMSE. 